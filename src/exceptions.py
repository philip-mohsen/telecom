from typing import Tuple

class InvalidGroupMemberTypeError(Exception):
    error_code = "INVALID_GROUP_MEMBER_TYPE"

    def __init__(self, member: object, allowed_types: Tuple[type]) -> None:
        self.member = member
        self.allowed_types = allowed_types
        self.message = f"Cannot add member of type {type(member).__name__} to the group. Allowed types: {', '.join(t.__name__ for t in allowed_types)}"
        super().__init__(self.message)