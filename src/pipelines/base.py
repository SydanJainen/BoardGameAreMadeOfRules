from abc import ABC, abstractmethod
from typing import Any, Optional

from src.core.models import ProcessedContent, RawContent


class AbstractPipeline(ABC):
    def __init__(
        self,
        data_adapter,
        llm_client,
        prompt_strategy,
        preprocessor=None,
    ):
        self.data_adapter = data_adapter
        self.llm_client = llm_client
        self.prompt_strategy = prompt_strategy
        self.preprocessor = preprocessor

    def execute(self, **kwargs) -> Any:
        raw_content = self.load_data()
        text = self.extract_content(raw_content)
        text = self.preprocess(text)
        processed = self.process_with_llm(text, **kwargs)
        result = self.format_result(processed, raw_content, **kwargs)

        return result

    def preprocess(self, text: str) -> str:
        if self.preprocessor:
            return self.preprocessor.preprocess(text)
        return text

    @abstractmethod
    def load_data(self) -> RawContent:
        """Load data from source."""

    @abstractmethod
    def extract_content(self, raw_content: RawContent) -> str:
        """Extract text from raw content."""

    def process_with_llm(self, text: str, **kwargs) -> ProcessedContent:
        prompt = self.prompt_strategy.build_prompt(text, **kwargs)
        if hasattr(self.llm_client, "generate_with_metadata"):
            response, execution_metadata = self.llm_client.generate_with_metadata(prompt)
        else:
            response = self.llm_client.generate(prompt)
            execution_metadata = None

        return ProcessedContent(
            text=response,
            raw_response=response,
            confidence=1.0,
            metadata={"prompt_length": len(prompt)},
            execution_metadata=execution_metadata,
        )

    @abstractmethod
    def format_result(
        self, processed: ProcessedContent, raw_content: RawContent, **kwargs
    ) -> Any:
        """Format final result."""
