from src.shared.application.uuid_generator import generate_uuid
from src.service_catalog.domain.model import Channel
from src.service_catalog.infrastructure.repositories.channel_repository import ChannelRepository

class CreateChannelUseCase:
    def __init__(self, channel_repository: ChannelRepository):
        self.channel_repository = channel_repository

    def execute(self, name: str) -> Channel:
        """Create a new channel and add it to the repository"""
        uuid =  generate_uuid(prefix="CH-")
        channel = Channel(uuid=uuid, name=name)
        self.channel_repository.add(channel)
        return channel
