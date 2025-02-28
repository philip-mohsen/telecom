class DomainException(Exception):
    def __init__(self, error_code: str, message: str) -> None:
        super().__init__(message)
        self.error_code = error_code

class InvalidNodeEntityTypeError(DomainException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="INVALID_NODE_ENTITY_TYPE", message=message)

class InvalidRootEntityTypeError(DomainException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="INVALID_ROOT_ENTITY_TYPE", message=message)

class InvalidParentEntityTypeError(DomainException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="INVALID_PARENT_ENTITY_TYPE", message=message)
