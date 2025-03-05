from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Tuple
from src.shared.domain.specifications.specification import Specification
from src.shared.domain.specifications.validation_error import ValidationError

@dataclass(frozen=True)
class TypeSpecification(Specification[Any]):
    allowed_types: Tuple[type, ...]
    allow_none: bool = False

    def is_satisfied_by(self, candidate: Any) -> ValidationError:
        if candidate is None:
            return ValidationError(is_valid=self.allow_none, error_messages=("The value cannot be None.",))
        return ValidationError(
            is_valid=isinstance(candidate, self.allowed_types),
            error_messages=(f"The value must be an instance of {self.allowed_types}.",)
            )
