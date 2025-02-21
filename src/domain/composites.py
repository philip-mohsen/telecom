"""
This module defines the TechnologyComposite class
which extends EntityComposite for Technology entities.
It includes validation for the type of components that can be added to the composite.
"""
from __future__ import annotations
from exceptions import InvalidEntityComponentTypeError
from .model import Technology
from .model import EntityComposite

class TechnologyComposite(EntityComposite[Technology]):
    def validate_entity_component_type(self, component: Technology | TechnologyComposite) -> None:
        if not isinstance(component, (Technology, TechnologyComposite)):
            raise InvalidEntityComponentTypeError(component, (Technology, TechnologyComposite))
