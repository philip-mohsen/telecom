from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.domain.model import Channel

class ChannelMapper(JSONMapper[Channel]):
    """Mapper for Channel domain object."""
    @staticmethod
    def to_dict(obj: Channel) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
        }

    @staticmethod
    def from_dict(data: dict) -> Channel:
        return Channel(
            uuid=data["uuid"],
            name=data["name"],
        )
