from dataclasses import dataclass
from typing import Any, Tuple
from src.shared.domain.specifications.specification import Specification
from src.shared.domain.specifications.validation_error import ValidationError

@dataclass(frozen=True)
class TypeSpecification(Specification[Any]):
    allowed_types: Tuple[type, ...]

    def is_satisfied_by(self, candidate: Any) -> ValidationError:
        return ValidationError(
            is_valid=isinstance(candidate, self.allowed_types),
            error_messages=(f"The value must be an instance of {self.allowed_types}.",)
            )
