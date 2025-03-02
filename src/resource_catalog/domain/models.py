from typing import Optional
from typing import Any
from src.shared.domain.models import Entity
from src.shared.domain.models import Category
from src.shared.domain.validation.category_validations import CategoryValidator
from src.shared.domain.models import CharacteristicSpecification

class ResourceSpecification(Entity):
    def __init__(self, uuid: str, name: str) -> None:
        super().__init__(uuid=uuid)
        self.name = name
        self.characteristics: dict[str, CharacteristicSpecification] = {}
        self.resource_category: Optional[ResourceCategory] = None

    def add_characteristic(self, characteristic: CharacteristicSpecification) -> None:
        self.characteristics[characteristic.uuid] = characteristic

    def remove_characteristic(self, characteristic: CharacteristicSpecification) -> None:
        self.characteristics.pop(characteristic.uuid)

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name}, "
            f"characteristics={self.characteristics})"
        )

class ResourceCategory(Category[ResourceSpecification]):
    def create_category_validator(self) -> CategoryValidator:
        validator = CategoryValidator(
            member_category_types=(ResourceSpecification,)
            )
        return validator

    def _add_member(self, entity: ResourceSpecification) -> None:
        resource_specification = entity
        resource_specification.resource_category = self
        self.members.append(resource_specification)

class Resource(Entity):
    def __init__(self, uuid: str, name: str, resource_specification: ResourceSpecification) -> None:
        super().__init__(uuid=uuid)
        self.name = name
        self.resource_specification = resource_specification
        self.characteristics_values: dict[str, Any] = {}

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name}, "
            f"resource_specification={self.resource_specification})"
        )
