from __future__ import annotations
from typing import TypeVar
from typing import Protocol
from typing import runtime_checkable
from typing_extensions import Self

ValueObjectT = TypeVar("ValueObjectT")

@runtime_checkable
class ValueObjectContract(Protocol[ValueObjectT]):
    value: ValueObjectT

    def __eq__(self, other: Self) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __str__(self) -> str:
        ...

@runtime_checkable
class EntityContract(Protocol):
    uuid: str

    def __eq__(self, other: Self) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __str__(self) -> str:
        ...
