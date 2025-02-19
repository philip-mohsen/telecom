from abc import ABC
from abc import abstractmethod

class EntityGroup(ABC):
    def __init__(self, node: object, parent=None) -> None:
        self.validate_node_type(node)
        self.members = []
        self.node = node
        self.parent = parent

    @abstractmethod
    def validate_node_type(self, node: object) -> None:
        pass

    def add(self, member: object) -> None:
        if not isinstance(member, EntityGroup):
            member = self.__class__(node=member, parent=self)
        self.members.append(member)

    @property
    def uuid(self) -> str:
        if self.parent:
            return f"{self.parent.uuid}.{self.node.uuid}"
        return self.node.uuid

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uuid == other.uuid

    def __str__(self, level: int = 0) -> str:
        indent = "  " * level
        return f"{indent}{self.node}\n" + "".join(member.__str__(level + 1) for member in self.members)

class Technology:
    def __init__(self, uuid: str, name: str, abbreviation: str = None) -> None:
        self.uuid = uuid
        self.name = name
        self.abbreviation = abbreviation
    
    def __str__(self) -> str:
        if self.abbreviation:
            return f"{self.__class__.__name__}({self.name}, {self.abbreviation})"
        return f"{self.__class__.__name__}({self.name})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Technology):
            return False
        return self.uuid == other.uuid
    
    def __hash__(self) -> int:
        return hash(self.uuid)