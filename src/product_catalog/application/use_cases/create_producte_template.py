from src.shared.application.uuid_generator import generate_uuid
from src.product_catalog.domain.model import ProductTemplate
from src.product_catalog.repositories.product_template_repository import ProductTemplateRepository
from src.product_catalog.repositories.product_content_repository import ProductContentRepository

class CreateProductTemplateUseCase:
    def __init__(self, product_template_repository: ProductTemplateRepository, product_content_repository: ProductContentRepository):
        self.template_repo = product_template_repository
        self.content_repo = product_content_repository

    def execute(self, name: str, content_uuids: list[str]) -> ProductTemplate:
        contents = [self.content_repo.get_by_uuid(uuid) for uuid in content_uuids]
        template = ProductTemplate(uuid=generate_uuid(prefix="PT-"), name=name, product_contents=contents)
        self.template_repo.add(template)
        return template
