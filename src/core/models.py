from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, field_validator


class ExecutionMetadata(BaseModel):
    model_config = {"protected_namespaces": ()}

    model_name: str = Field(..., description="LLM model name")
    model_alias: Optional[str] = Field(None, description="Model alias if configured")
    temperature: float = Field(default=0.7, description="Temperature parameter")
    timestamp: str = Field(..., description="Execution timestamp")
    execution_time_seconds: float = Field(..., description="Execution time in seconds")
    tokens: Optional[int] = Field(None, description="Token count if available")
    prompt_length: int = Field(default=0, description="Length of prompt in characters")
    additional_params: Dict[str, Any] = Field(
        default_factory=dict, description="Additional model parameters"
    )

    @classmethod
    def create(
        cls,
        model_name: str,
        execution_time: float,
        model_alias: Optional[str] = None,
        temperature: float = 0.7,
        tokens: Optional[int] = None,
        prompt_length: int = 0,
        **additional_params
    ) -> "ExecutionMetadata":
        return cls(
            model_name=model_name,
            model_alias=model_alias,
            temperature=temperature,
            timestamp=datetime.utcnow().isoformat() + "Z",
            execution_time_seconds=round(execution_time, 2),
            tokens=tokens,
            prompt_length=prompt_length,
            additional_params=additional_params,
        )

    def to_yaml_dict(self) -> Dict[str, Any]:

        data = {
            "model": self.model_name,
            "temperature": self.temperature,
            "timestamp": self.timestamp,
            "execution_time_seconds": self.execution_time_seconds,
            "prompt_length": self.prompt_length,
        }

        if self.model_alias and self.model_alias != self.model_name:
            data["model_alias"] = self.model_alias

        if self.tokens is not None:
            data["tokens"] = self.tokens

        if self.additional_params:
            data["additional_params"] = self.additional_params

        return data


class Audience(str, Enum):
    CHILD = "child"
    ADULT = "adult"
    EXPERT = "expert"


class RawContent(BaseModel):
    text: str = Field(..., description="Raw rulebook text")
    source_type: str = Field(..., description="Source type: pdf, text, bgg, etc.")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata (filename, size, etc.)",
    )

    @field_validator("text")
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Text cannot be empty")
        return v


class ProcessedContent(BaseModel):
    text: str = Field(..., description="Processed text from LLM")
    raw_response: str = Field(..., description="Raw LLM response")
    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="LLM confidence score (0-1)",
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata (prompt length, response time, etc.)",
    )
    execution_metadata: Optional[ExecutionMetadata] = Field(
        default=None,
        description="Metadata about model execution (model name, timing, tokens, etc.)",
    )



class AnalysisResult(BaseModel):
    mechanics: List[str] = Field(
        ..., description="Meccaniche del gioco (deck-building, worker placement, ecc.)"
    )
    complexity: float = Field(
        ..., ge=1.0, le=5.0, description="Complessità da 1 (Uno) a 5 (Twilight Imperium)"
    )
    min_players: int = Field(
        ..., ge=1, description="Minimo numero di giocatori - almeno 1, anche i solitari contano"
    )
    max_players: int = Field(..., ge=1, description="Massimo numero di giocatori")
    duration_min: int = Field(..., ge=1, description="Durata media in minuti")

    bgg_mechanics: Optional[List[str]] = Field(
        default=None, description="Meccaniche secondo BoardGameGeek"
    )
    bgg_complexity: Optional[float] = Field(
        default=None, ge=1.0, le=5.0, description="Complessità BGG (weight)"
    )
    bgg_players: Optional[str] = Field(default=None, description="Range giocatori BGG tipo '2-4'")
    bgg_duration: Optional[int] = Field(default=None, ge=1, description="Durata BGG in minuti")

    mechanics_similarity: Optional[float] = Field(
        default=None, ge=0.0, le=1.0, description="Similarità meccaniche LLM vs BGG (0-1)"
    )
    complexity_error: Optional[float] = Field(
        default=None, description="Errore assoluto sulla complessità"
    )
    overall_score: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Score complessivo di quanto l'LLM ci ha azzeccato (0-1)",
    )

    execution_metadata: Optional[ExecutionMetadata] = Field(
        default=None, description="Metadata about model execution"
    )
    raw_response: Optional[str] = Field(
        default=None, description="Raw LLM response before parsing/formatting"
    )

    @field_validator("max_players")
    @classmethod
    def max_gte_min(cls, v: int, info) -> int:
        min_players = info.data.get("min_players")
        if min_players and v < min_players:
            raise ValueError(
                f"Il massimo giocatori ({v}) non può essere minore del minimo ({min_players})"
            )
        return v


class ExplanationResult(BaseModel):
    explanation: str = Field(..., description="La spiegazione delle regole")
    audience: Audience = Field(..., description="A chi è rivolta la spiegazione")
    execution_metadata: Optional[ExecutionMetadata] = Field(
        default=None, description="Metadata about model execution"
    )
    raw_response: Optional[str] = Field(
        default=None, description="Raw LLM response before parsing/formatting"
    )

    @field_validator("explanation")
    @classmethod
    def explanation_not_empty(cls, v: str) -> str:
        """Una spiegazione vuota non serve a nessuno."""
        if not v or not v.strip():
            raise ValueError("La spiegazione non può essere vuota")
        return v.strip()


class FixRulesResult(BaseModel):
    identified_issues: List[str] = Field(
        default_factory=list, description="Lista dei problemi trovati nel regolamento"
    )
    suggested_fixes: List[str] = Field(
        default_factory=list, description="Correzioni suggerite per ogni problema"
    )
    corrected_rules: str = Field(..., description="Regolamento corretto completo")
    execution_metadata: Optional[ExecutionMetadata] = Field(
        default=None, description="Metadata about model execution"
    )
    raw_response: Optional[str] = Field(
        default=None, description="Raw LLM response before parsing/formatting"
    )


class InventResult(BaseModel):
    game_name: str = Field(..., description="Nome del gioco inventato")
    theme: str = Field(..., description="Tema/ambientazione del gioco")
    mechanics: List[str] = Field(default_factory=list, description="Meccaniche utilizzate")
    rules: str = Field(..., description="Regolamento completo del gioco")
    components: List[str] = Field(
        default_factory=list, description="Lista dei componenti necessari (carte, dadi, plance...)"
    )
    player_count: str = Field(..., description="Range giocatori tipo '2-4' o '3-6'")
    duration: str = Field(..., description="Durata stimata tipo '30-45 minuti'")
    execution_metadata: Optional[ExecutionMetadata] = Field(
        default=None, description="Metadata about model execution"
    )
    raw_response: Optional[str] = Field(
        default=None, description="Raw LLM response before parsing/formatting"
    )

    @field_validator("game_name", "rules")
    @classmethod
    def required_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Questo campo non può essere vuoto")
        return v.strip()


class MoveRecommendation(BaseModel):
    current_state: str = Field(..., description="Stato di gioco attuale come descritto dall'utente")
    recommended_move: str = Field(..., description="La mossa consigliata")
    reasoning: str = Field(..., description="Perché questa mossa è una buona idea")
    alternative_moves: List[str] = Field(
        default_factory=list, description="Altre mosse possibili, se non ti convince la prima"
    )
    execution_metadata: Optional[ExecutionMetadata] = Field(
        default=None, description="Metadata about model execution"
    )
    raw_response: Optional[str] = Field(
        default=None, description="Raw LLM response before parsing/formatting"
    )

    @field_validator("current_state", "recommended_move", "reasoning")
    @classmethod
    def required_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Questo campo è obbligatorio")
        return v.strip()


