from typing import Tuple

class InvalidEntityComponentTypeError(Exception):
    error_code = "INVALID_ENTITY_COMPONENT_TYPE"

    def __init__(self, member: object, allowed_types: Tuple[type]) -> None:
        self.member = member
        self.allowed_types = allowed_types
        self.message = (
            f"Cannot add member of type {type(member).__name__} to the composite. "
            f"Allowed types: {', '.join(t.__name__ for t in allowed_types)}"
        )
        super().__init__(self.message)

class MissingRequiredTechnologyError(Exception):
    error_code = "MISSING_REQUIRED_TECHNOLOGY"

    def __init__(self) -> None:
        self.message = "A service must have at least one required technology."
        super().__init__(self.message)
