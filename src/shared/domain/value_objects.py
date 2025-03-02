from __future__ import annotations
from dataclasses import dataclass
from typing import Generic
from src.shared.domain.contracts import ValueObjectT

@dataclass(frozen=True)
class ValueObject(Generic[ValueObjectT]):
    value: ValueObjectT
