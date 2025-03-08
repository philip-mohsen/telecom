from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
from src.shared.domain.specifications.specification import Specification
from src.shared.domain.specifications.specification_result import SpecificationResult


@dataclass(frozen=True)
class UniqueSpecification(Specification[Sequence]):
    def is_satisfied_by(self, candidate: Sequence) -> SpecificationResult:
        return SpecificationResult(
            is_valid=len(candidate) == len(set(candidate)),
            error_messages=("The elements in the sequence must be unique.",)
            )
