from __future__ import annotations
from .model import Technology
from .model import EntityComposite
from exceptions import InvalidEntityComponentTypeError

class TechnologyComposite(EntityComposite[Technology]):
    def validate_entity_component_type(self, component: Technology | TechnologyComposite) -> None:
        if not isinstance(component, (Technology, TechnologyComposite)):
            raise InvalidEntityComponentTypeError(component, (Technology, TechnologyComposite))