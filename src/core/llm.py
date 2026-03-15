import logging
import time
from typing import Any, Dict, List, Optional, Tuple

import requests
from jsonschema import ValidationError, validate

from src.core.models import ExecutionMetadata

logger = logging.getLogger(__name__)


MODEL_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "base_url": {"type": "string"},
        "timeout": {"type": "integer", "minimum": 1},
        "models": {
            "type": "object",
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "required": ["alias"],
                    "properties": {
                        "alias": {"type": "string"},
                        "description": {"type": "string"},
                        "task_affinity": {"type": "array", "items": {"type": "string"}},
                        "context_window": {"type": "integer", "minimum": 512},
                        "temperature_default": {"type": "number", "minimum": 0.0, "maximum": 2.0},
                        "enabled": {"type": "boolean"},
                    },
                }
            },
        },
        "default_model": {"type": "string"},
    },
    "required": ["base_url", "models", "default_model"],
}


def validate_ollama_config(config: dict) -> None:
    try:
        validate(instance=config, schema=MODEL_CONFIG_SCHEMA)
    except ValidationError as e:
        raise ValueError(f"Invalid Ollama configuration: {e.message}")


class OllamaModelClient:

    def __init__(
        self,
        model_name: str,
        base_url: str = "http://localhost:11434",
        timeout: int = 180,
        config: dict = None,
        alias: Optional[str] = None,
    ):
        self.model_name = model_name
        self.alias = alias or model_name
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.config = config or {}
        self.task_affinity = self.config.get("task_affinity", [])
        self.context_window = self.config.get("context_window", 4096)
        self.temperature_default = self.config.get("temperature_default", 0.7)
        self.num_predict = self.config.get("num_predict", -1)

    def generate(self, prompt: str) -> str:
        response_text, _ = self.generate_with_metadata(prompt)
        return response_text

    def generate_with_metadata(self, prompt: str) -> Tuple[str, ExecutionMetadata]:
        start_time = time.time()

        try:
            options = {
                "temperature": self.temperature_default,
                "num_predict": self.num_predict,
                "num_ctx": self.context_window,
            }
            logger.debug(
                "Ollama API request for model '%s' with options: %s",
                self.model_name,
                options,
            )

            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False,
                    "options": options,
                },
                timeout=self.timeout,
            )
            response.raise_for_status()

            execution_time = time.time() - start_time
            response_data = response.json()
            response_text = response_data.get("response", "")

            tokens = None
            if "eval_count" in response_data:
                tokens = response_data["eval_count"]

            metadata = ExecutionMetadata.create(
                model_name=self.model_name,
                model_alias=self.alias,
                execution_time=execution_time,
                temperature=self.temperature_default,
                tokens=tokens,
                prompt_length=len(prompt),
            )

            return response_text, metadata

        except requests.exceptions.ConnectionError as e:
            raise ConnectionError(
                f"Cannot reach server Ollama at {self.base_url}. " f"Try using: 'ollama serve'"
            ) from e

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise RuntimeError(
                    f"Model '{self.model_name}' not found. "
                    f"Use 'ollama pull {self.model_name}'"
                ) from e
            raise RuntimeError(f"HTTP error: {e}") from e

    def health_check(self) -> bool:
        try:
            available_models = self.list_models()
            return self.model_name in available_models
        except Exception:
            return False

    def list_models(self) -> List[str]:
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            response.raise_for_status()
            models = response.json().get("models", [])
            return [m["name"] for m in models if "name" in m]
        except Exception as e:
            raise RuntimeError(f"Cannot list models: {e}") from e


class LocalModelRegistry:
    def __init__(self, ollama_config: dict):
        self.config = ollama_config
        self.base_url = ollama_config.get("base_url", "http://localhost:11434")
        self.timeout = ollama_config.get("timeout", 180)
        self.default_model_name = ollama_config.get("default_model", "llama3.2:latest")
        self.models: Dict[str, OllamaModelClient] = {}
        self._initialise_models()

    def _initialise_models(self):
        models_config = self.config.get("models", {})

        for model_name, model_config in models_config.items():
            if not model_config.get("enabled", True):
                continue

            alias = model_config["alias"]
            client = OllamaModelClient(
                model_name=model_name,
                base_url=self.base_url,
                timeout=self.timeout,
                config=model_config,
                alias=alias,
            )
            self.models[alias] = client

    def get_model(self, alias: str) -> Optional[OllamaModelClient]:
        return self.models.get(alias)

    def get_default_model(self) -> OllamaModelClient:
        for model in self.models.values():
            if model.model_name == self.default_model_name:
                return model
        if self.models:
            return next(iter(self.models.values()))

        raise RuntimeError(f"No models available in registry")

    def get_all_models(self) -> List[OllamaModelClient]:
        return list(self.models.values())

    def get_models_by_task(self, task_type: str) -> List[OllamaModelClient]:
        matching = [model for model in self.models.values() if task_type in model.task_affinity]

        matching.sort(key=lambda m: len(m.task_affinity))

        return matching

    def health_check_all(self) -> Dict[str, bool]:
        results = {}
        for alias, model in self.models.items():
            results[alias] = model.health_check()
        return results
