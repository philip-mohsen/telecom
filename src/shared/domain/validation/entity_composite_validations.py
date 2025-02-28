from src.shared.exceptions.domain_exceptions import InvalidNodeEntityTypeError
from src.shared.exceptions.domain_exceptions import InvalidRootEntityTypeError
from src.shared.exceptions.domain_exceptions import InvalidParentEntityTypeError
from src.shared.domain.contracts import EntityContract

class EntityCompositeValidator:
    def __init__(
            self,
            node_entity_types: tuple[type[EntityContract], ...],
            root_entity_types: tuple[type[EntityContract], ...],
            parent_entity_types: tuple[type[EntityContract], ...]) -> None:

        self.node_entity_types = node_entity_types
        self.root_entity_types = root_entity_types
        self.parent_entity_types = parent_entity_types

    def validate_node_entity_type(self, node: EntityContract) -> None:
        if not isinstance(node, self.node_entity_types):
            raise InvalidNodeEntityTypeError(f"Invalid node type: {type(node)}")

    def validate_root_entity_type(self, root: EntityContract) -> None:
        if not isinstance(root, self.root_entity_types):
            raise InvalidRootEntityTypeError(f"Invalid root type: {type(root)}")

    def validate_parent_entity_type(self, parent: EntityContract) -> None:
        if not isinstance(parent, self.parent_entity_types):
            raise InvalidParentEntityTypeError(f"Invalid parent type: {type(parent)}")
