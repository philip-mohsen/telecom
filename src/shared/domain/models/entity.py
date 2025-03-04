from dataclasses import dataclass
from typing import TypeVar
from typing import Any

EntityT = TypeVar("EntityT", bound="Entity")

@dataclass(frozen=True)
class Entity:
    uuid: str

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid

    def __hash__(self) -> int:
        return hash(self.uuid)
