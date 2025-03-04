from dataclasses import dataclass
from typing import TypeVar, Generic
from typing import Any

ValueT = TypeVar("ValueT")

@dataclass(frozen=True)
class ValueObject(Generic[ValueT]):
    value: ValueT

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.value == other.value
        return False

    def __hash__(self) -> int:
        return hash(self.value)
