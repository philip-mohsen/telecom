from abc import ABC
from abc import abstractmethod
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
        return self.name == other.name and self.abbreviation == other.abbreviation
    
    def __hash__(self) -> int:
        return hash(self.name)