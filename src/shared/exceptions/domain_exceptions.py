from src.shared.exceptions.base import BaseException

class InvalidNodeEntityTypeError(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="INVALID_NODE_ENTITY_TYPE", message=message)

class InvalidRootEntityTypeError(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="INVALID_ROOT_ENTITY_TYPE", message=message)

class InvalidParentEntityTypeError(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="INVALID_PARENT_ENTITY_TYPE", message=message)
