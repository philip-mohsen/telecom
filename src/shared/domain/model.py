from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
import hashlib

SimpleValueT = TypeVar("SimpleValueT")
EntityComponentT = TypeVar("EntityComponentT", bound="EntityComponent")

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

class SimpleValueObject(ValueObject, Generic[SimpleValueT]):
    def __init__(self, value: SimpleValueT) -> None:
        self._value = value

    @property
    def value(self) -> SimpleValueT:
        return self._value

    def _equal_values(self, other: SimpleValueObject[SimpleValueT]) -> bool:
        return self.value == other.value

    def _hash_values(self) -> int:
        return hash(self.value)

class Entity(ABC):
    def __init__(self, uuid: str) -> None:
        self.uuid = uuid

    def __eq__(self, other: Entity) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid

    def __hash__(self) -> int:
        return hash(self.uuid)

    @abstractmethod
    def __str__(self) -> str:
        pass

class NamedEntity(Entity):
    def __init__(self, uuid: str, name: str) -> None:
        super().__init__(uuid=uuid)
        self.name = name

class EntityComponent:
    def __init__(self, entity: Entity, label: str = None) -> None:
        self.entity = entity
        self.label = label
        self._parent: EntityComposite | None = None

    @property
    def name(self) -> str:
        """
        Returns the entity's name if it has one, or the provided label otherwise.
        Uses getattr to handle both NamedEntity and regular Entity instances.
        """
        return getattr(self.entity, "name", self.label)

    @property
    def parent(self) -> EntityComposite | None:
        return self._parent

    @parent.setter
    def parent(self, parent: EntityComposite) -> None:
        self._parent = parent

    @property
    def uuid(self) -> str:
        return self.entity.uuid

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"  # Overriding the __str__ method

class EntityComposite(Generic[EntityComponentT]):
    def __init__(self, name: str) -> None:
        self.name = name
        self.members: set[EntityComponentT] = set()

    @abstractmethod
    def validate_entity_component_type(self, component: EntityComponentT) -> None:
        pass

    def _add_validated_component(self, component: EntityComponentT) -> None:
        self.members.add(component)
        component.parent = self

    def add(self, component: T) -> None:
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

class Category(NamedEntity):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
