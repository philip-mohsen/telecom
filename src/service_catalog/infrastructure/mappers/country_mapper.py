from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.domain.model import Country

class CountryMapper(JSONMapper[Country]):
    """Mapper for Country domain object."""
    @staticmethod
    def to_dict(obj: Country) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
        }

    @staticmethod
    def from_dict(data: dict) -> Country:
        return Country(
            uuid=data["uuid"],
            name=data["name"],
        )
