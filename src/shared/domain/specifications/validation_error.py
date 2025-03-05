from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ValidationError:
    is_valid: bool = True
    error_messages: tuple[str, ...] = tuple()

    def __and__(self, other: ValidationError) -> ValidationError:
        if all([self.is_valid, other.is_valid]):
            return ValidationError()

        error_messages = tuple(sorted(set(self.error_messages + other.error_messages)))
        return ValidationError(is_valid=False, error_messages=error_messages)

    def __or__(self, other: ValidationError) -> ValidationError:
        if any([self.is_valid, other.is_valid]):
            return ValidationError()

        error_messages = tuple(sorted(set(self.error_messages + other.error_messages)))
        return ValidationError(is_valid=False, error_messages=error_messages)

    def __invert__(self) -> ValidationError:
        return ValidationError(
            is_valid=not self.is_valid,
            error_messages=tuple(reversed(["NOT " + message for message in self.error_messages]))
            )
