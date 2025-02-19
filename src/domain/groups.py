from __future__ import annotations
from typing import Union
from .model import Group
from .model import Technology
from exceptions import InvalidGroupMemberTypeError

class TechnologyGroup(Group):
    def validate_node_type(self, node: object) -> None:
        if not isinstance(node, (Technology,)):
            raise InvalidGroupMemberTypeError(node, (Technology,))

# class TechnologyGroup(Group):
#     def __init__(self, metadata: Technology) -> None:
#         super().__init__()
#         self.validate_member_type(metadata, (Technology,))
#         self.metadata = metadata

#     def add(self, member: Union[TechnologyGroup, Technology]) -> None:
#         self.validate_member_type(member, (TechnologyGroup, Technology))
#         self.members.append(member)
    
#     def __str__(self, level: int = 0) -> str:
#         indent = "  " * level
#         result = f"{indent}{self.metadata}\n"
#         for member in self.members:
#             if isinstance(member, Technology):
#                 result += f"{indent}  {member}\n"
#             else:
#                 result += member.__str__(level + 1)
#         return result