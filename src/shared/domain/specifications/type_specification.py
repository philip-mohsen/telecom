from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Tuple
from src.shared.domain.specifications.specification import Specification

@dataclass(frozen=True)
class TypeSpecification(Specification[Any]):
    allowed_types: Tuple[type, ...]
    allow_none: bool = False

    def is_satisfied_by(self, candidate: Any) -> bool:
        if candidate is None:
            return self.allow_none
        return isinstance(candidate, self.allowed_types)
