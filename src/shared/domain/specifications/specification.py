from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic
from typing import Any, Callable

T = TypeVar("T")

class Specification(ABC, Generic[T]):
    """Base class for all specifications."""

    @abstractmethod
    def is_satisfied_by(self, candidate: T) -> bool:
        """Checks if the candidate satisfies the specification."""
        pass

    def __and__(self, other: Any) -> Specification[T]:
        """Combines this specification with another using logical AND."""
        return AndSpecification(self, other)

    def __or__(self, other: Any) -> Specification[T]:
        """Combines this specification with another using logical OR."""
        return OrSpecification(self, other)

    def __invert__(self) -> Specification[T]:
        """Negates this specification."""
        return NotSpecification(self)

    def __call__(self, candidate: T) -> bool:
        """Allows the specification to be called like a function."""
        return self.is_satisfied_by(candidate)

@dataclass(frozen=True)
class AndSpecification(Specification[T]):
    """Specification that combines two specifications using logical AND."""
    left: Specification[T]
    right: Specification[T]

    def is_satisfied_by(self, candidate: T) -> bool:
        return self.left.is_satisfied_by(candidate) and self.right.is_satisfied_by(candidate)

@dataclass(frozen=True)
class OrSpecification(Specification[T]):
    """Specification that combines two specifications using logical OR."""
    left: Specification[T]
    right: Specification[T]

    def is_satisfied_by(self, candidate: T) -> bool:
        return self.left.is_satisfied_by(candidate) or self.right.is_satisfied_by(candidate)

@dataclass(frozen=True)
class NotSpecification(Specification[T]):
    """Specification that negates another specification."""
    specification: Specification[T]

    def is_satisfied_by(self, candidate: T) -> bool:
        return not self.specification.is_satisfied_by(candidate)

@dataclass(frozen=True)
class LambdaSpecification(Specification[T]):
    """Specification that uses a lambda function or callable to define the criteria."""
    predicate: Callable[[T], bool]

    def is_satisfied_by(self, candidate: T) -> bool:
        return self.predicate(candidate)
