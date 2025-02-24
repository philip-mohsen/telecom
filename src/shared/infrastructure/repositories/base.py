from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

EntityT = TypeVar('EntityT')  # Generic type for entities

class Repository(ABC, Generic[EntityT]):
    """
    Base repository class for common repository operations.
    """

    @abstractmethod
    def add(self, entity: EntityT) -> None:
        """Adds an entity to the repository."""
        pass

    @abstractmethod
    def get_by_uuid(self, uuid: str) -> Optional[EntityT]:
        """Retrieves an entity by its UUID."""
        pass

    @abstractmethod
    def update(self, entity: EntityT) -> None:
        """Updates an entity in the repository."""
        pass

    @abstractmethod
    def delete(self, uuid: str) -> None:
        """Deletes an entity from the repository by its UUID."""
        pass

    @abstractmethod
    def get_all(self) -> list[EntityT]:
        """Retrieves all entities from the repository"""
        pass
