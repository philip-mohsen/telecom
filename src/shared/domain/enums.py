from enum import Enum

class ValueType(Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    TIME = "time"
    OBJECT = "object"
    ARRAY = "array"
    NULL = "null"
