from dataclasses import dataclass
from typing import Any
from src.shared.domain.specifications.specification import Specification
from src.shared.domain.specifications.specification_result import SpecificationResult

@dataclass(frozen=True)
class TypeSpecification(Specification[Any]):
    allowed_types: tuple[type, ...]

    def is_satisfied_by(self, candidate: Any) -> SpecificationResult:
        return SpecificationResult(
            is_valid=isinstance(candidate, self.allowed_types),
            error_messages=(f"The value must be an instance of {self.allowed_types}.",)
            )
