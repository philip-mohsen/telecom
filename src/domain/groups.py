from __future__ import annotations
from typing import Union
from .model import Group
from .model import Technology
from exceptions import InvalidGroupMemberTypeError

class TechnologyGroup(Group):
    def validate_node_type(self, node: object) -> None:
        if not isinstance(node, (Technology,)):
            raise InvalidGroupMemberTypeError(node, (Technology,))