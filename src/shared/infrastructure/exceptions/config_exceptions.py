from enum import Enum

class ConfigErrorCode(Enum):
    CONFIG_FILE_NOT_FOUND = "CONFIG_FILE_NOT_FOUND"
    CONFIG_SECTION_NOT_FOUND = "CONFIG_SECTION_NOT_FOUND"
    INVALID_CONFIG_VALUE = "INVALID_CONFIG_VALUE"
    DATABASE_URI_SCHEME_NOT_FOUND = "DATABASE_URI_SCHEME_NOT_FOUND"

class ConfigFileNotFound(Exception):
    def __init__(self, message: str = "Configuration file not found"):
        super().__init__(message)
        self.error_code = ConfigErrorCode.CONFIG_FILE_NOT_FOUND

class ConfigSectionNotFound(Exception):
    def __init__(self, message: str = "Configuration section not found"):
        super().__init__(message)
        self.error_code = ConfigErrorCode.CONFIG_SECTION_NOT_FOUND

class InvalidConfigValue(Exception):
    def __init__(self, message: str = "Invalid configuration value"):
        super().__init__(message)
        self.error_code = ConfigErrorCode.INVALID_CONFIG_VALUE

class DatabaseURISchemeNotFound(Exception):
    def __init__(self, message: str = "Database URI scheme not found"):
        super().__init__(message)
        self.error_code = ConfigErrorCode.DATABASE_URI_SCHEME_NOT_FOUND
