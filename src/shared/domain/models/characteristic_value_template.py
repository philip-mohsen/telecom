from dataclasses import dataclass
from enum import Enum
from typing import Optional
from typing import Generic, TypeVar
from datetime import date

ValueT = TypeVar("ValueT")

class DataType(Enum):
    STRING = 'string'
    INTEGER = 'integer'
    FLOAT = 'float'
    BOOLEAN = 'boolean'
    DATE = 'date'

@dataclass(frozen=True)
class CharacteristicValueTemplate(Generic[ValueT]):
    data_type: DataType
    allowed_values: Optional[set[ValueT]] = None

@dataclass(frozen=True)
class StringCharacteristicValueTemplate(CharacteristicValueTemplate[str]):
    data_type: DataType = DataType.STRING
    regex: Optional[str] = None

@dataclass(frozen=True)
class IntegerCharacteristicValueTemplate(CharacteristicValueTemplate[int]):
    data_type: DataType = DataType.INTEGER
    min_value: Optional[int] = None
    max_value: Optional[int] = None

@dataclass(frozen=True)
class FloatCharacteristicValueTemplate(CharacteristicValueTemplate[float]):
    data_type: DataType = DataType.FLOAT
    min_value: Optional[float] = None
    max_value: Optional[float] = None

@dataclass(frozen=True)
class BooleanCharacteristicValueTemplate(CharacteristicValueTemplate[bool]):
    data_type: DataType = DataType.BOOLEAN
    allowed_values: Optional[set[bool]] = {True, False}

@dataclass(frozen=True)
class DateCharacteristicValueTemplate(CharacteristicValueTemplate[date]):
    data_type: DataType = DataType.DATE
    format: Optional[str] = None
