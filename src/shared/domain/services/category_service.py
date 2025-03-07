import inspect
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence
from src.shared.domain.specifications import Specification
from src.shared.domain.specifications import TypeSpecification
from src.shared.domain.specifications import UniqueSpecification
from src.shared.domain.models import EntityT
from src.shared.domain.models import Category

@dataclass(frozen=True)
class CategoryService(ABC):
    @classmethod
    @abstractmethod
    def get_member_type(cls) -> type[EntityT]:
        pass

    @classmethod
    def get_member_specification(cls) -> Specification[EntityT]:
        return TypeSpecification((cls.get_member_type(),))

    @classmethod
    def get_constructor_specification(cls) -> dict[str, Specification[Any]]:
        return {
            "uuid": TypeSpecification((str,)),
            "name": TypeSpecification((str,)),
            "description": TypeSpecification((str, None,)),
            "members": TypeSpecification((tuple,)) & UniqueSpecification()
        }

    def create_category(
            self,
            uuid: str,
            name: str,
            description: Optional[str],
            members: Sequence[EntityT] = ()
    ) -> Category[EntityT]:
        constructor_specification = self.get_constructor_specification()
        signature = inspect.signature(Category.__init__)
        kwargs = dict(uuid=uuid, name=name, description=description, members=members)

        for name in signature.parameters.keys():
            if name == "self":
                continue

            if name not in constructor_specification:
                continue

            value = kwargs[name]
            validation = constructor_specification[name](value)

            if not validation.is_valid:
                raise ValueError(f"Invalid value for {name}: {validation.error_message}")

        return Category(uuid=uuid, name=name, description=description, members=members)

    def add_member(self, category: Category[EntityT], member: EntityT) -> Category[EntityT]:
        member_specification: Specification[EntityT] = self.get_member_specification()
        members_unique_specification = UniqueSpecification()

        member_specification_result = member_specification(member)
        members_unique_specification_result = members_unique_specification(tuple(category.members) + (member,))

        if not member_specification_result.is_valid:
            raise ValueError("Invalid member type: " + member_specification_result.error_message)

        if not members_unique_specification_result.is_valid:
            raise ValueError("Member already exists in category")

        return category.add_member(member)
