from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.domain.value_objects import DataLimitValue

class DataLimitValueMapper(JSONMapper[DataLimitValue]):
    @staticmethod
    def to_dict(obj: DataLimitValue) -> dict:
        return {
            "value": obj.value,
        }

    @staticmethod
    def from_dict(data: dict) -> DataLimitValue:
        return DataLimitValue(
            value=data["value"]
            )
