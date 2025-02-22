from .base import JSONMapper
from src.service_catalog.domain.model import TechnologyService
from src.service_catalog.repositories.technology_repository import TechnologyRepository

class TechnologyServiceMapper(JSONMapper[TechnologyService]):
    """Mapper for TechnologyService domain object."""
    @staticmethod
    def to_dict(obj: TechnologyService) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
            "technologies": [tech.uuid for tech in obj.technologies],
        }

    @staticmethod
    def from_dict(data: dict, technology_repository: TechnologyRepository) -> TechnologyService:
        return TechnologyService(
            uuid=data["uuid"],
            name=data["name"],
            technologies=[technology_repository.get_by_uuid(uuid) for uuid in data["technologies"]],
        )
