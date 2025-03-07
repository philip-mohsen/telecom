from dataclasses import dataclass
from typing import Sequence, Tuple
from src.shared.domain.specifications.specification import Specification
from src.shared.domain.specifications.validation_error import ValidationError

@dataclass(frozen=True)
class SequenceSpecification(Specification[Sequence]):
    allowed_sequence_type: type[Sequence]
    allowed_item_types: Tuple[type, ...]
    min_length: int = 0

    def is_satisfied_by(self, candidate: Sequence) -> ValidationError:
        if not isinstance(candidate, self.allowed_sequence_type):
            return ValidationError(
                is_valid=False,
                error_messages=(
                    f"Expected a sequence of type {self.allowed_sequence_type.__name__}, "
                    f"but received {type(candidate).__name__}.")
                )

        if len(candidate) < self.min_length:
            return ValidationError(
                is_valid=False,
                error_messages=(
                    f"Sequence must contain at least {self.min_length} item(s), "
                    f"but found {len(candidate)}.")
                )

        if not all(isinstance(item, self.allowed_item_types) for item in candidate):
            return ValidationError(
                is_valid=False,
                error_messages=(f"All items in the sequence must be of type(s) "
                                f"{', '.join(t.__name__ for t in self.allowed_item_types)}. "
                                "Found items with invalid types.")
                )
