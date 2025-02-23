from src.product_catalog.domain.model import ProductContent
from src.product_catalog.repositories.product_content_repository import ProductContentRepository
from src.service_catalog.repositories.technology_service_repository import TechnologyServiceRepository
from src.shared.application.uuid_generator import generate_uuid

class CreateProductContentUseCase:
    def __init__(self, product_content_repo: ProductContentRepository, technology_service_repo: TechnologyServiceRepository):
        self.product_content_repo = product_content_repo
        self.technology_service_repo = technology_service_repo

    def execute(self, name: str, service_uuid: str) -> ProductContent:
        service = self.technology_service_repo.get_by_uuid(service_uuid)
        product_content = ProductContent(uuid=generate_uuid(prefix="PC-"), name=name, service=service)
        self.product_content_repo.add(product_content)
        return product_content
