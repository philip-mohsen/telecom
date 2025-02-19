from abc import ABC
from abc import abstractmethod
from typing import Sequence


class Group(ABC):
    def __init__(self, node, parent=None) -> None:
        self.validate_node_type(node)
        self.members = []
        self.node = node
        self.parent = parent

    @abstractmethod
    def validate_node_type(self, node: object) -> None:
        pass

    def add(self, member: object) -> None:
        if not isinstance(member, Group):
            member = self.__class__(member, parent=self)
        self.members.append(member)
    
    def __str__(self, level: int = 0) -> str:
        indent = "  " * level
        result = f"{indent}{self.node}\n"
        for member in self.members:
            result += member.__str__(level + 1)
        return result

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