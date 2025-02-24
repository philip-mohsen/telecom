"""
Mappers for domain object (for JSON persistance demo).
"""
from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.domain.model import Technology

class TechnologyMapper(JSONMapper[Technology]):
    """Mapper for Technology domain object."""
    @staticmethod
    def to_dict(obj: Technology) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
            "abbreviation": obj.abbreviation,
        }

    @staticmethod
    def from_dict(data: dict) -> Technology:
        return Technology(
            uuid=data["uuid"],
            name=data["name"],
            abbreviation=data["abbreviation"],
        )
