from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from typing import Optional, Generic, TypeVar
import hashlib

class ValueObject(ABC):
    def __eq__(self, other: ValueObject) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._equal_values(other)
    
    def __hash__(self) -> int:
        return self._hash_values()
    
    @abstractmethod
    def _equal_values(self, other: ValueObject) -> bool:
        pass

    @abstractmethod
    def _hash_values(self) -> int:
        pass

class Entity(ABC):
    def __init__(self, uuid: str) -> None:
        self.uuid = uuid

    def __eq__(self, other: Entity) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid
    
    def __hash__(self) -> int:
        return hash(self.uuid)
    
class EntityComponent(Entity):
    def __init__(self, uuid: str, name: str) -> None:
        super().__init__(uuid)
        self.name = name
        self._parent = None
    
    @property
    def parent(self) -> Optional[EntityComponentType]:
        return self._parent
    
    @parent.setter
    def parent(self, parent: Optional[EntityComponentType]) -> None:
        self._parent = parent

EntityComponentType = TypeVar('EntityComponentType', bound=EntityComponent)

class EntityComposite(EntityComponent, Generic[EntityComponentType]):
    def __init__(self, name: str) -> None:
        self.name = name
        self.members: set[EntityComponentType] = set()

    @abstractmethod
    def validate_entity_component_type(self, component: EntityComponentType) -> None:
        pass

    def add(self, component: EntityComponentType) -> None:
        self.validate_entity_component_type(component)
        self.members.add(component)
        component.parent = self

    @property
    def uuid(self) -> str: # Overriding the uuid property
        sorted_uuids = sorted(member.uuid for member in self.members)   # Sorting the UUIDs
        combined_uuids = "".join(sorted_uuids)  # Combining the UUIDs
        return hashlib.sha256(combined_uuids.encode()).hexdigest()  # Hashing the combined UUIDs
    
    def __str__(self) -> str:
            member_strings = ", ".join(str(member) for member in self.members)
            return f"{self.__class__.__name__}(name={self.name}, members=[{member_strings}])"

class Technology(EntityComponent):
    def __init__(self, uuid: str, name: str, abbreviation: str = None) -> None:
        super().__init__(uuid=uuid, name=name)
        self.abbreviation = abbreviation

    def __str__(self) -> str:
        if self.abbreviation:
            return f"{self.__class__.__name__}(name='{self.name}', abbreviation='{self.abbreviation}')"
        return f"{self.__class__.__name__}(name='{self.name}')"