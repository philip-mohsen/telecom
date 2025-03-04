from __future__ import annotations
from dataclasses import dataclass, field, replace
from typing import Generic
from typing import Optional, Sequence
from src.shared.domain.models.entity import Entity
from src.shared.domain.models.entity import EntityT

@dataclass(eq=False, frozen=True)
class Category(Entity, Generic[EntityT]):
    name: str
    description: Optional[str] = None
    members: Sequence[EntityT] = field(default_factory=tuple)

    def add_member(self, member: EntityT) -> Category[EntityT]:
        return replace(self, members=tuple(list(self.members) + [member]))
