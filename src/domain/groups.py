from __future__ import annotations
from .model import EntityGroup
from .model import Technology
from exceptions import InvalidGroupMemberTypeError

class TechnologyGroup(EntityGroup):
    def validate_node_type(self, node: object) -> None:
        if not isinstance(node, (Technology,)):
            raise InvalidGroupMemberTypeError(node, (Technology,))