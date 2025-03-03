from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any
from typing_extensions import Self

class BaseSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: Any) -> bool:
        pass

    def __call__(self, candidate: Any) -> bool:
        return self.is_satisfied_by(candidate)

    def __and__(self, other: BaseSpecification) -> BaseSpecification:
        return AndSpecification(self, other)

    def __or__(self, other: BaseSpecification) -> BaseSpecification:
        return OrSpecification(self, other)

    def __neg__(self) -> BaseSpecification:
        return NotSpecification(self)

@dataclass(frozen=True)
class AndSpecification(BaseSpecification):
    left: BaseSpecification
    right: BaseSpecification

    def is_satisfied_by(self, candidate: Any) -> bool:
        return self.left(candidate) and self.right(candidate)

@dataclass(frozen=True)
class OrSpecification(BaseSpecification):
    left: BaseSpecification
    right: BaseSpecification

    def is_satisfied_by(self, candidate: Any) -> bool:
        return self.left(candidate) or self.right(candidate)

@dataclass(frozen=True)
class NotSpecification(BaseSpecification):
    specification: BaseSpecification

    def is_satisfied_by(self, candidate: Any) -> bool:
        return not self.specification(candidate)

@dataclass(frozen=True)
class RequiredSpecification(BaseSpecification):
    def is_satisfied_by(self, candidate: Any) -> bool:
        return candidate is not None

@dataclass(frozen=True)
class TypeSpecification(BaseSpecification):
    allowed_types: tuple[type, ...]
    allow_none: bool = False

    def is_satisfied_by(self, candidate: Any) -> bool:
        if candidate is None:
            return self.allow_none
        return isinstance(candidate, self.allowed_types)

@dataclass(frozen=True)
class CombinedSpecification(BaseSpecification):
    specifications: list[BaseSpecification] = field(default_factory=list)

    def is_satisfied_by(self, candidate: Any) -> bool:
        return all(specification(candidate) for specification in self.specifications)

@dataclass(frozen=True)
class SpecificationBuilder:
    specifications: list[BaseSpecification] = field(default_factory=list)

    def add(self, specification: BaseSpecification) -> Self:
        self.specifications.append(specification)
        return self

    def build(self) -> CombinedSpecification:
        return CombinedSpecification(self.specifications)
