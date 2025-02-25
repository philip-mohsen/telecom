from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.infrastructure.repositories.technology_service_repository import TechnologyServiceRepository
from src.product_catalog.domain.model import ProductTemplate

class ProductTemplateMapper(JSONMapper[ProductTemplate]):
    @staticmethod
    def to_dict(product_template: ProductTemplate) -> dict:
        return {
            "uuid": product_template.uuid,
            "name": product_template.name,
            "services": [service.uuid for service in product_template.services],
        }

    @staticmethod
    def from_dict(data: dict, technology_service_repository: TechnologyServiceRepository) -> ProductTemplate:
        services = [technology_service_repository.get_by_uuid(uuid) for uuid in data["services"]]
        return ProductTemplate(
            uuid=data["uuid"],
            name=data["name"],
            services=services,
        )
