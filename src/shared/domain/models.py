from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar
from typing import Generic
from typing import Optional
from typing import Iterator
from typing import Any
from typing_extensions import Self
import hashlib
from src.shared.domain.contracts import ValueObjectT
from src.shared.domain.validation.entity_composite_validations import EntityCompositeValidator

EntityT = TypeVar("EntityT", bound="Entity")

class ValueObject(Generic[ValueObjectT]):
    def __init__(self, value: ValueObjectT) -> None:
        self._value = value

    @property
    def value(self) -> ValueObjectT:
        return self._value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"

class Entity:
    def __init__(self, uuid: str) -> None:
        self.uuid = uuid

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(uuid={self.uuid})"

class Category(Entity):
    def __init__(self, uuid: str, name: str) -> None:
        super().__init__(uuid=uuid)
        self.name = name

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(uuid={self.uuid}, name={self.name})"

class EntityComposite(ABC, Generic[EntityT]):
    def __init__(self, entity: EntityT, label: Optional[str] = None) -> None:
        self.parent: Optional[Self] = None
        self.members: list[Self] = []
        self.validator = self.create_entity_composite_validator()
        self.validate(entity)
        self.entity = entity
        self.label = label
        self.depth = 0

    @abstractmethod
    def create_entity_composite_validator(self) -> EntityCompositeValidator:
        pass

    @property
    def name(self) -> Optional[str]:
        return getattr(self.entity, "name", self.label)

    @property
    def uuid(self) -> str:
        sorted_uuids = sorted(node.entity.uuid for node in self.dfs())
        combined_uuids = "".join(sorted_uuids)
        return hashlib.sha256(combined_uuids.encode()).hexdigest()

    def dfs(self) -> Iterator[Self]:
        yield self
        for member in self.members:
            yield from member.dfs()

    def validate(self, entity: EntityT) -> None:
        self.validator.validate_node_entity_type(entity)

        if not self.parent:
            self.validator.validate_root_entity_type(entity)

        if self.parent:
            self.validator.validate_parent_entity_type(self.parent.entity)

    def add(self, entity: EntityT, label: Optional[str] = None) -> Self:
        self.validate(entity)
        member = self.__class__(entity=entity, label=label)
        member.parent = self
        member.depth = self.depth + 1
        self.members.append(member)
        return member

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __str__(self) -> str:
        member_strings = []
        for node in self.dfs():
            indent = " " * node.depth
            node_str = (
                f"{indent}{self.__class__.__name__}("
                f"entity={node.entity}, label={node.label})"
            )
            member_strings.append(node_str)
        return "\n".join(member_strings)
