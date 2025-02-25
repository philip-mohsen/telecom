from __future__ import annotations
from src.shared.domain.model import ValueObject
from src.shared.domain.model import SimpleValueObject

class MinuteValue(ValueObject):
    def __init__(self, value: int, location_uuid: str, destination_uuid: str) -> None:
        self.value = value
        self.location_uuid = location_uuid
        self.destination_uuid = destination_uuid

    def _equal_values(self, other: MinuteValue) -> bool:
        return (
            self.value == other.value and
            self.location_uuid == other.location_uuid and
            self.destination_uuid == other.destination_uuid
        )

    def _hash_values(self) -> int:
        return hash((self.value, self.location_uuid, self.destination_uuid))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value}, location_uuid={self.location}, destination_uuid={self.destination})"

class DataLimitValue(SimpleValueObject[int]):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"

class ChannelValue(SimpleValueObject[str]):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"
