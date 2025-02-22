"""
Mappers for domain object (for JSON persistance demo).
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

ObjectT = TypeVar("ObjectT")

class JSONMapper(ABC, Generic[ObjectT]):
    """Abstract class for JSON mappers."""

    @staticmethod
    @abstractmethod
    def to_dict(obj: ObjectT) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_dict(self, data: dict) -> ObjectT:
        pass
