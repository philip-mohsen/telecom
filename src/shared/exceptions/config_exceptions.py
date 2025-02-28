from src.shared.exceptions.base import BaseException

class ConfigSectionNotFound(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="CONFIG_SECTION_NOT_FOUND", message=message)

class DatabaseURISchemeNotFound(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(error_code="DATABASE_URI_SCHEME_NOT_FOUND", message=message)
