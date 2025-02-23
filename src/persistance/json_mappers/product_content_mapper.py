from src.product_catalog.domain.model import ProductContent
from src.service_catalog.repositories.technology_service_repository import TechnologyServiceRepository
from src.persistance.json_mappers.base import JSONMapper

class ProductContentMapper(JSONMapper[ProductContent]):
    """Mapper for ProductContent domain object."""
    @staticmethod
    def to_dict(obj: ProductContent) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
            "service": obj.service.uuid,
        }

    @staticmethod
    def from_dict(data: dict, technology_service_repository: TechnologyServiceRepository) -> ProductContent:
        return ProductContent(
            uuid=data["uuid"],
            name=data["name"],
            service=technology_service_repository.get_by_uuid(data["service"]),
        )
