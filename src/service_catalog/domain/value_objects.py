from __future__ import annotations
from src.shared.domain.model import SimpleValueObject

class MinuteValue(SimpleValueObject[int]):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value} minutes)"

class MessageCountValue(SimpleValueObject[int]):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value} messages)"

class DataLimitValue(SimpleValueObject[int]):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value} MB)"

class InternetSpeedValue(SimpleValueObject[int]):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value} Mbps)"

class TVPackageValue(SimpleValueObject[str]):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"
