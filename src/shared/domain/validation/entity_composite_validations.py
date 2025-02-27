from src.shared.domain.contracts import EntityContract

class EntityCompositeValidator:
    def __init__(
            self,
            node_entity_types: tuple[type[EntityContract], ...],
            parent_entity_types: tuple[type[EntityContract], ...]) -> None:

        self.node_entity_types = node_entity_types
        self.parent_entity_types = parent_entity_types

    def validate_node_entity_type(self, node: EntityContract) -> None:
        if not isinstance(node, self.node_entity_types):
            raise TypeError(f"Invalid node type: {type(node)}")

    def validate_parent_entity_type(self, parent: EntityContract) -> None:
        if not isinstance(parent, self.parent_entity_types):
            raise TypeError(f"Invalid parent type: {type(parent)}")
