from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from typing import Union
from exceptions import InvalidGroupMemberTypeError

class Group(ABC):
    def __init__(self, name: str, members: list = None) -> None:
        self.name = name
        self.members = members or []

    @abstractmethod
    def add(self, member: object) -> None:
        pass

class Technology:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Technology):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.name)

class TechnologyGroup(Group):
    def add(self, member: Union[TechnologyGroup, Technology]) -> None:
        if not isinstance(member, (TechnologyGroup, Technology)):
            raise InvalidGroupMemberTypeError(member, (TechnologyGroup, Technology))
        
        self.members.append(member)