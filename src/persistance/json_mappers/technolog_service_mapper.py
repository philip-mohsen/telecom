from .base import JSONMapper
from service_catalog.domain.model import TechnologService
from service_catalog.repositories.technology_repository import TechnologyRepository

class TechnologyServiceMapper(JSONMapper[TechnologService]):
    """Mapper for TechnologyEnabledService domain object."""
    @staticmethod
    def to_dict(obj: TechnologService) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
            "technologies": [tech.uuid for tech in obj.technologies],
        }

    @staticmethod
    def from_dict(data: dict, technology_repository: TechnologyRepository) -> TechnologService:
        return TechnologService(
            uuid=data["uuid"],
            name=data["name"],
            technologies=[technology_repository.get_by_uuid(uuid) for uuid in data["technologies"]],
        )
