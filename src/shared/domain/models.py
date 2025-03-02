from __future__ import annotations
from dataclasses import dataclass
from dataclasses import field
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Optional
from typing import TypeVar
from typing import Generic
from src.shared.domain.validation.category_validations import CategoryValidator

EntityT = TypeVar("EntityT", bound="Entity")
CategoryT = TypeVar("CategoryT", bound="Category")
CategoryComponentT = TypeVar("CategoryComponentT", bound="CategoryComponent")

@dataclass
class Entity:
    _uuid: str

    @property
    def uuid(self) -> str:
        return self._uuid

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid

    def __hash__(self) -> int:
        return hash(self.uuid)

@dataclass(eq=False)
class Category(Entity, ABC, Generic[EntityT]):
    name: str
    description: Optional[str] = None
    members: list[EntityT] = field(default_factory=list)

    @abstractmethod
    def _add(self, member: EntityT) -> None:
        pass

    def add(self, member: EntityT) -> None:
        self._add(member)

@dataclass(eq=False)
class CategoryComposite(Category, ABC, Generic[CategoryT]):
    parent: Optional[CategoryT] = None
    sub_categories: list[CategoryComposite[CategoryT]] = field(default_factory=list)
    depth: int = 0

    @abstractmethod
    def _add(self, sub_category: CategoryComposite[CategoryT]) -> None:
        pass

    def add(self, sub_category: CategoryComposite[CategoryT]) -> None:
        self._add(sub_category)

@dataclass(eq=False)
class CategoryComponent(Category, Generic[CategoryT]):
    category: CategoryT
    parent: Optional[CategoryT] = None
    depth: int = 0

@dataclass(eq=False)
class CategoryComposite(CategoryComponent, Generic[CategoryComponentT]):
    children: list[CategoryComponentT] = field(default_factory=list)

    def add(self, component: CategoryComposite[CategoryComponentT]) -> None:
        component.parent = self
        component.depth = self.depth + 1
        self.children.append(component)
