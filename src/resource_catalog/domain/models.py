from typing import Optional
from src.shared.domain.models import Entity
from src.shared.domain.models import EntityComposite
from src.shared.domain.models import Category
from src.shared.domain.validation.entity_composite_validations import EntityCompositeValidator

class Technology(Entity):
    def __init__(self, uuid: str, name: str, abbreviation: Optional[str] = None) -> None:
        super().__init__(uuid=uuid)
        self.name = name
        self.abbreviation = abbreviation

    def __str__(self) -> str:
        if self.abbreviation:
            return (
                f"{self.__class__.__name__}(name={self.name}, "
                f"abbreviation={self.abbreviation})"
            )
        return f"{self.__class__.__name__}(name={self.name})"

class TechnologyTree(EntityComposite[Technology]):
    def create_entity_composite_validator(self) -> EntityCompositeValidator:
        validator = EntityCompositeValidator(
            node_entity_types = (Category, Technology),
            root_entity_types = (Category,),
            parent_entity_types = (Category,)
        )
        return validator
