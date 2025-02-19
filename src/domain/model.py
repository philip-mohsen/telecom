from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from typing import Union
from typing import Sequence
from exceptions import InvalidGroupMemberTypeError

class Group(ABC):
    def __init__(self) -> None:
        self.members = []

    @abstractmethod
    def add(self, member: object) -> None:
        pass
    
    @staticmethod
    def validate_member_type(member: object, allowed_types: Sequence[type]) -> None:
        if not isinstance(member, allowed_types):
            raise InvalidGroupMemberTypeError(member, allowed_types)

class Technology:
    def __init__(self, name: str, abbreviation: str = None) -> None:
        self.name = name
        self.abbreviation = abbreviation
    
    def __str__(self) -> str:
        if self.abbreviation:
            return f"{self.__class__.__name__}({self.name}, {self.abbreviation})"
        return f"{self.__class__.__name__}({self.name})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Technology):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.name)

class TechnologyGroup(Group):
    def __init__(self, metadata: Technology) -> None:
        self.validate_member_type(metadata, (Technology,))
        super().__init__()
        self.metadata = metadata

    def add(self, member: Union[TechnologyGroup, Technology]) -> None:
        self.validate_member_type(member, (TechnologyGroup, Technology))
        self.members.append(member)
    
    def __str__(self, level: int = 0) -> str:
        indent = "  " * level
        result = f"{indent}{self.metadata}\n"
        for member in self.members:
            if isinstance(member, Technology):
                result += f"{indent}  {member}\n"
            else:
                result += member.__str__(level + 1)
        return result