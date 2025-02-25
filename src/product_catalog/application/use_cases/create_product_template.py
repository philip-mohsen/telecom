from src.shared.application.uuid_generator import generate_uuid
from src.service_catalog.infrastructure.repositories.technology_service_repository import TechnologyServiceRepository
from src.product_catalog.domain.model import ProductTemplate
from src.product_catalog.infrastructure.repositories.product_template_repository import ProductTemplateRepository

class CreateProductTemplateUseCase:
    def __init__(
            self,
            product_template_repository: ProductTemplateRepository,
            technology_service_repository: TechnologyServiceRepository) -> None:
        self.product_template_repository = product_template_repository
        self.technology_service_repository = technology_service_repository

    def execute(self, name: str, service_uuids: list[str]) -> ProductTemplate:
        services = [self.technology_service_repository.get_by_uuid(uuid) for uuid in service_uuids]
        template = ProductTemplate(uuid=generate_uuid(prefix="PT-"), name=name, services=services)
        self.product_template_repository.add(template)
        return template
