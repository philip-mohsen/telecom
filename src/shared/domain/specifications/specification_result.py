from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class SpecificationResult:
    is_valid: bool = True
    error_messages: tuple[str, ...] = tuple()

    def __and__(self, other: SpecificationResult) -> SpecificationResult:
        messages = tuple(sorted(set(self.error_messages + other.error_messages)))
        return SpecificationResult(
            is_valid=self.is_valid and other.is_valid,
            error_messages=messages
        )

    def __or__(self, other: SpecificationResult) -> SpecificationResult:
        messages = tuple(sorted(set(self.error_messages + other.error_messages)))
        return SpecificationResult(
            is_valid=self.is_valid or other.is_valid,
            error_messages=messages
        )

    def __invert__(self) -> SpecificationResult:
        messages = tuple(reversed(["NOT " + message for message in self.error_messages]))
        return SpecificationResult(
            is_valid=not self.is_valid,
            error_messages=messages
        )

    @property
    def error_message(self) -> str:
        return ", ".join(self.error_message)
