from src.shared.infrastructure.repositories.base import Repository
from src.shared.infrastructure.json_db import JSONDatabase
from src.service_catalog.domain.model import Channel
from src.service_catalog.infrastructure.mappers.channel_mapper import ChannelMapper

class ChannelRepository(Repository[Channel]):
    def __init__(self, json_db: JSONDatabase):
        self.json_db = json_db
        self.data = self.json_db.load_data("channels")

    def add(self, channel: Channel) -> None:
        self.data[channel.uuid] = ChannelMapper.to_dict(channel)
        self.json_db.save_data("channels", self.data)

    def get_by_uuid(self, uuid: str) -> Channel:
        data = self.data.get(uuid)
        if data is None:
            raise KeyError(f"Channel with uuid {uuid} not found.")
        return ChannelMapper.from_dict(data)

    def update(self, channel: Channel) -> None:
        pass

    def delete(self, uuid: str) -> None:
        pass

    def get_all(self) -> list[Channel]:
        pass
