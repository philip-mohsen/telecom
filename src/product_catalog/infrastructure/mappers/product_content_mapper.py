from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.infrastructure.repositories.technology_service_repository import TechnologyServiceRepository
from src.product_catalog.domain.model import ProductContent

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
