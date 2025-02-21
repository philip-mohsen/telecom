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
        self._parent: EntityComposite | None = None
    
    @property
    def parent(self) -> EntityComposite | None:
        return self._parent
    
    @parent.setter
    def parent(self, parent: EntityComposite) -> None:
        self._parent = parent

TEntityComponent = TypeVar("TEntityComponent", bound="EntityComponent")

class EntityComposite(EntityComponent, Generic[TEntityComponent]):
    def __init__(self, name: str) -> None:
        self.name = name
        self.members: set[TEntityComponent] = set()

    @abstractmethod
    def validate_entity_component_type(self, component: TEntityComponent) -> None:
        pass

    def _add_validated_component(self, component: TEntityComponent) -> None:
        self.members.add(component)
        component.parent = self

    def add(self, component: TEntityComponent) -> None:
        self.validate_entity_component_type(component)
        self._add_validated_component(component)

    @property
    def uuid(self) -> str: # Overriding the uuid property
        sorted_uuids = sorted(member.uuid for member in self.members)   # Sorting the UUIDs
        combined_uuids = "".join(sorted_uuids)  # Combining the UUIDs
        return hashlib.sha256(combined_uuids.encode()).hexdigest()  # Hashing the combined UUIDs
    
    def __str__(self) -> str:
        sorted_members = sorted(self.members, key=lambda x: x.uuid)  # Sorting the members by UUID
        member_strings = ", ".join(str(member) for member in sorted_members)
        return f"{self.__class__.__name__}(name='{self.name}', members=[{member_strings}])"

class Technology(EntityComponent):
    def __init__(self, uuid: str, name: str, abbreviation: str = None) -> None:
        super().__init__(uuid=uuid, name=name)
        self.abbreviation = abbreviation

    def __str__(self) -> str:
        if self.abbreviation:
            return f"{self.__class__.__name__}(name='{self.name}', abbreviation='{self.abbreviation}')"
        return f"{self.__class__.__name__}(name='{self.name}')"