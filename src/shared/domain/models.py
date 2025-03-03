from __future__ import annotations
from dataclasses import dataclass, field, replace
from typing import Any, Optional, Sequence
from typing import TypeVar, Generic
from src.shared.domain.contracts import EntityContract, CategoryContract

EntityT = TypeVar("EntityT", bound="Entity")

@dataclass(frozen=True)
class Entity(EntityContract):
    uuid: str

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid

    def __hash__(self) -> int:
        return hash(self.uuid)

@dataclass(eq=False, frozen=True)
class Category(Entity, CategoryContract[EntityT, EntityT], Generic[EntityT]):
    name: str
    description: Optional[str] = None
    members: Sequence[EntityT] = field(default_factory=tuple)

    def add(self, member: EntityT) -> Category[EntityT]:
        return replace(self, members=tuple(list(self.members) + [member]))
