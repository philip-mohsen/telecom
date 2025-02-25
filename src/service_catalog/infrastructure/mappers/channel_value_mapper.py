from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.domain.value_objects import ChannelValue

class ChannelValueMapper(JSONMapper[ChannelValue]):
    @staticmethod
    def to_dict(obj: ChannelValue) -> dict:
        return {
            "value": obj.value,
        }

    @staticmethod
    def from_dict(data: dict) -> ChannelValue:
        return ChannelValue(
            value=data["value"]
        )
