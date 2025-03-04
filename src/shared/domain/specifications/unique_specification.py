from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
from src.shared.domain.specifications.specification import Specification

@dataclass(frozen=True)
class UniqueSpecification(Specification[Sequence]):
    def is_satisfied_by(self, candidate: Sequence) -> bool:
        return len(candidate) == len(set(candidate))
