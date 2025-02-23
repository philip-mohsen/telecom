from src.service_catalog.domain.model import TechnologyService
from src.service_catalog.domain.enums import ContentValueType
from src.service_catalog.repositories.technology_repository import TechnologyRepository
from .base import JSONMapper

class TechnologyServiceMapper(JSONMapper[TechnologyService]):
    """Mapper for TechnologyService domain object."""
    @staticmethod
    def to_dict(obj: TechnologyService) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
            "technologies": [tech.uuid for tech in obj.technologies],
            "content_value_type": obj.content_value_type.value,
        }

    @staticmethod
    def from_dict(data: dict, technology_repository: TechnologyRepository) -> TechnologyService:
        return TechnologyService(
            uuid=data["uuid"],
            name=data["name"],
            technologies=[technology_repository.get_by_uuid(uuid) for uuid in data["technologies"]],
            content_value_type=ContentValueType(data["content_value_type"]),
        )
