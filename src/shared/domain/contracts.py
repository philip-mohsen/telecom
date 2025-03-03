from __future__ import annotations
from typing import TypeVar
from typing import Protocol, runtime_checkable
from typing import Any, Sequence, Optional
from typing import ClassVar
from src.shared.domain.specifications import BaseSpecification

ValueObjectT = TypeVar("ValueObjectT")
EntityT_co = TypeVar("EntityT_co", bound="EntityContract", covariant=True)
EntityT_contra = TypeVar("EntityT_contra", bound="EntityContract", contravariant=True)
CategoryT = TypeVar("CategoryT", bound="CategoryContract")

@runtime_checkable
class ValueObjectContract(Protocol[ValueObjectT]):
    value: ValueObjectT

    def __eq__(self, other: Any) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __str__(self) -> str:
        ...

@runtime_checkable
class EntityContract(Protocol):
    uuid: str

    def __eq__(self, other: Any) -> bool:
        ...

    def __hash__(self) -> int:
        ...

@runtime_checkable
class CategoryContract(EntityContract, Protocol[EntityT_co, EntityT_contra]):
    name: str
    description: Optional[str]

    @property
    def members(self) -> Sequence[EntityT_co]:
        ...

    def add(self, member: EntityT_contra) -> CategoryContract[EntityT_co, EntityT_contra]:
        ...

@runtime_checkable
class CategoryServiceContract(Protocol[EntityT_contra, CategoryT]):
    uuid_specification: ClassVar[BaseSpecification]
    name_specification: ClassVar[BaseSpecification]
    description_specification: ClassVar[BaseSpecification]
    members_specification: ClassVar[BaseSpecification]
    category_member_specification: ClassVar[BaseSpecification]

    def validate_constructor_attribute(
            self,
            attribute_name: str,
            attribute_value: Any,
            attribute_specification: BaseSpecification
            ) -> None:
        ...

    def validate_category_member(self, member: EntityT_contra) -> None:
        ...

    def create_category(
            self,
            uuid: str,
            name: str,
            description: Optional[str] = None,
            members: Sequence[EntityT_contra] = ()
            ) -> CategoryT:
        ...

    def add_category_member(
            self,
            category: CategoryT,
            member: EntityT_contra) -> CategoryT:
        ...
