from src.shared.exceptions.base import BaseException

class InvalidCategoryMemberTypeError(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="INVALID_CATEGORY_MEMBER_TYPE", message=message)
