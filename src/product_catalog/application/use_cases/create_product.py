from src.shared.application.uuid_generator import generate_uuid
from src.service_catalog.domain.value_objects import ValueObject
from src.product_catalog.domain.model import Product
from src.product_catalog.infrastructure.repositories.product_repository import ProductRepository
from src.product_catalog.infrastructure.repositories.product_template_repository import ProductTemplateRepository

class CreateProductUseCase:
    def __init__(
            self,
            product_repository: ProductRepository,
            product_template_repository: ProductTemplateRepository
    ) -> None:
        self.product_repository = product_repository
        self.product_template_repository = product_template_repository

    def execute(self, template_uuid: str, product_name: str, content_values: dict[str, ValueObject]) -> Product:
        template = self.product_template_repository.get_by_uuid(template_uuid)
        product = Product(uuid=generate_uuid(prefix="P-"), name=product_name, product_template=template)
        product.content_values = content_values
        self.product_repository.add(product)
        return product
