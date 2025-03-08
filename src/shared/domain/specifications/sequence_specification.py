from dataclasses import dataclass
from typing import Sequence
from src.shared.domain.specifications.specification import Specification
from src.shared.domain.specifications.specification_result import SpecificationResult

@dataclass(frozen=True)
class SequenceSpecification(Specification[Sequence]):
    allowed_sequence_types: tuple[type[Sequence], ...]
    allowed_item_types: tuple[type, ...]
    min_length: int = 0

    def is_satisfied_by(self, candidate: Sequence) -> SpecificationResult:
        if not isinstance(candidate, self.allowed_sequence_types):
            error_message = (
                f"Expected a sequence of type(s) {', '.join(t.__name__ for t in self.allowed_sequence_types)}, "
                f"but received {type(candidate).__name__}."
            )

            return SpecificationResult(
                is_valid=False,
                error_messages=(error_message,)
            )

        if len(candidate) < self.min_length:
            error_message = (
                f"Sequence must contain at least {self.min_length} item(s), "
                f"but found {len(candidate)}."
            )

            return SpecificationResult(
                is_valid=False,
                error_messages=(error_message,)
            )

        if not all(isinstance(item, self.allowed_item_types) for item in candidate):
            error_message = (
                f"All items in the sequence must be of type(s) "
                f"{', '.join(t.__name__ for t in self.allowed_item_types)}. "
                "Found items with invalid types."
            )

            return SpecificationResult(
                is_valid=False,
                error_messages=(error_message,)
            )

        return SpecificationResult()
