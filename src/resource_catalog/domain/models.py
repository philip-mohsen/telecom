from src.shared.domain.models import Entity
from src.shared.domain.models import Category
from src.shared.domain.validation.category_validations import CategoryValidator

class ResourceSpecification(Entity):
    def __init__(self, uuid: str, name: str) -> None:
        super().__init__(uuid=uuid)
        self.name = name

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"

class ResourceCategory(Category[ResourceSpecification]):
    def create_category_validator(self) -> CategoryValidator:
        validator = CategoryValidator(
            member_category_types=(ResourceSpecification,)
            )
        return validator
