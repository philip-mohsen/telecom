from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.domain.value_objects import MinuteValue

class MinuteValueMapper(JSONMapper[MinuteValue]):
    @staticmethod
    def to_dict(obj: MinuteValue) -> dict:
        return {
            "value": obj.value,
            "location_uuid": obj.location_uuid,
            "destination_uuid": obj.destination_uuid,
        }

    @staticmethod
    def from_dict(data: dict) -> MinuteValue:
        return MinuteValue(
            value=data["value"],
            location_uuid=data["location_uuid"],
            destination_uuid=data["destination_uuid"],
        )
