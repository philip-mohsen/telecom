from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar
from typing import Generic
from typing import Optional
from typing import Any
from typing import Iterator
from src.shared.domain.contracts import ValueObjectT
from src.shared.domain.validation.category_validations import CategoryValidator

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

class Category(ABC, Entity, Generic[EntityT]):
    def __init__(self, uuid: str, name: str, description: Optional[str] = None) -> None:
        super().__init__(uuid=uuid)
        self.name = name
        self.description = description
        self.members: list[EntityT] = []
        self.parent: Optional[Category[EntityT]] = None
        self.subcategories: list[Category[EntityT]] = []
        self.depth = 0
        self.validator = self.create_category_validator()

    @abstractmethod
    def create_category_validator(self) -> CategoryValidator:
        pass

    def add_subcategory(
            self,
            uuid: str,
            name: str,
            description: Optional[str] = None
            ) -> Category[EntityT]:

        subcategory = self.__class__(uuid=uuid, name=name, description=description)
        subcategory.parent = self
        subcategory.depth = self.depth + 1
        self.subcategories.append(subcategory)
        return subcategory

    def add_member(self, entity: EntityT) -> None:
        self.validator.validate_category_member_type(entity)
        self.members.append(entity)

    def dfs(self) -> Iterator[Category[EntityT]]:
        yield self
        for subcategory in self.subcategories:
            yield from subcategory.dfs()

    def __str__(self) -> str:
        subcategory_strings = []
        for node in self.dfs():
            indent = " " * node.depth
            node_str = (
                f"{indent}{self.__class__.__name__}("
                f"name={node.name}, uuid={node.uuid}, description={node.description})"
            )
            subcategory_strings.append(node_str)
        return "\n".join(subcategory_strings)
