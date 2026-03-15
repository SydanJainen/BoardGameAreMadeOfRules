"""Pipeline for explaining game rules to different audiences."""

from typing import Any

from src.core.models import Audience, ExplanationResult, ProcessedContent, RawContent
from .base import AbstractPipeline


class ExplainPipeline(AbstractPipeline):

    def load_data(self) -> RawContent:
        return self.data_adapter.load()

    def extract_content(self, raw_content: RawContent) -> str:
        return raw_content.text

    def format_result(
        self, processed: ProcessedContent, raw_content: RawContent, **kwargs
    ) -> ExplanationResult:
        audience = kwargs.get("audience", Audience.ADULT)
        if isinstance(audience, str):
            audience = Audience(audience.lower())

        return ExplanationResult(
            explanation=processed.text,
            audience=audience,
            execution_metadata=processed.execution_metadata,
            raw_response=processed.raw_response,
        )
