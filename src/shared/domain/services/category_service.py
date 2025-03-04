from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence
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

    def validate_constructor_attribute(self, attribute_name: str, value: Any) -> None:
        specification = self.get_constructor_specification().get(attribute_name)
        if not specification(value):
            raise ValueError(f"Invalid value for {attribute_name}")

    def create_category(
            self,
            uuid: str,
            name: str,
            description: Optional[str],
            members: Sequence[EntityT] = ()
            ) -> Category[EntityT]:

        self.validate_constructor_attribute("uuid", uuid)
        self.validate_constructor_attribute("name", name)
        self.validate_constructor_attribute("description", description)
        self.validate_constructor_attribute("members", members)

        return Category(uuid=uuid, name=name, description=description, members=members)

    def add_member(self, category: Category[EntityT], member: EntityT) -> Category[EntityT]:
        member_specification: Specification[EntityT] = self.get_member_specification()

        if not member_specification(member):
            raise ValueError("Invalid member")

        return category.add_member(member)
