from src.shared.application.uuid_generator import generate_uuid
from src.service_catalog.domain.value_objects import SimpleValueObject
from src.product_catalog.domain.model import Product
from src.product_catalog.infrastructure.repositories.product_repository import ProductRepository
from src.product_catalog.infrastructure.repositories.product_template_repository import ProductTemplateRepository
from src.product_catalog.infrastructure.repositories.product_content_repository import ProductContentRepository

class CreateProductUseCase:
    def __init__(
            self,
            product_repository: ProductRepository,
            product_template_repository: ProductTemplateRepository,
            product_content_repository: ProductContentRepository):
        self.product_repo = product_repository
        self.template_repo = product_template_repository
        self.content_repo = product_content_repository

    def execute(self, template_uuid: str, product_name: str, content_values: dict[str, SimpleValueObject]) -> Product:
        template = self.template_repo.get_by_uuid(template_uuid)
        product = Product(uuid=generate_uuid(prefix="P-"), name=product_name, product_template=template)
        product.content_values = content_values
        self.product_repo.add(product)
        return product
