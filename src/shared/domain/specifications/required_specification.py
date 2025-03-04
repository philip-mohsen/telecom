from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from src.shared.domain.specifications.specification import Specification

@dataclass(frozen=True)
class RequiredSpecification(Specification[Any]):
    def is_satisfied_by(self, candidate: Any) -> bool:
        return candidate is not None
