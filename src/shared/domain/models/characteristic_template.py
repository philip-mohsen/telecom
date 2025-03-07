from dataclasses import dataclass
from typing import Optional
from src.shared.domain.models import Entity
from src.shared.domain.models.characteristic_value_template import CharacteristicValueTemplate

@dataclass(eq=False, frozen=True)
class CharacteristicTemplate(Entity):
    name: str
    description: Optional[str] = None
    configurable: bool = True
    is_unique: bool = False
    min_cardinality: int = 0
    max_cardinality: Optional[int] = None
    value_template: CharacteristicValueTemplate
