from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any
from src.shared.domain.specifications import Specification
from src.shared.domain.specifications import TypeSpecification
from src.shared.domain.models import EntityT
from src.shared.domain.models import Category

@dataclass(frozen=True)
class CategoryService(ABC):

    @abstractmethod
    @classmethod
    def get_member_specification(cls) -> Specification[EntityT]:
        pass

    @classmethod
    def get_constructor_specification(cls) -> dict[str, Specification[Any]]:
        return {
            "uuid": TypeSpecification((str,)),
            "name": TypeSpecification((str,)),
            "description": TypeSpecification((str,), allow_none=True),
            "members": TypeSpecification((tuple,))
        }

    def create_category(self, **kwargs) -> Category[EntityT]:
        constructor_specification = self.get_constructor_specification()
        for key, specification in constructor_specification.items():
            if not specification(kwargs.get(key)):
                raise ValueError(f"Invalid value for {key}")

        return Category(**kwargs)

    def add_member(self, category: Category[EntityT], member: EntityT) -> Category[EntityT]:
        member_specification: Specification[EntityT] = self.get_member_specification()
        if not member_specification(member):
            raise ValueError("Invalid member")

        return category.add_member(member)
