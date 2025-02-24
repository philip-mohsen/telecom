from src.shared.infrastructure.mappers.base import JSONMapper
from src.product_catalog.domain.model import ProductTemplate
from src.product_catalog.infrastructure.repositories.product_content_repository import ProductContentRepository

class ProductTemplateMapper(JSONMapper[ProductTemplate]):
    @staticmethod
    def to_dict(product_template: ProductTemplate) -> dict:
        return {
            "uuid": product_template.uuid,
            "name": product_template.name,
            "product_contents": [content.uuid for content in product_template.product_contents],
        }

    @staticmethod
    def from_dict(data: dict, product_content_repository: ProductContentRepository) -> ProductTemplate:
        product_contents = [product_content_repository.get_by_uuid(uuid) for uuid in data["product_contents"]]
        return ProductTemplate(
            uuid=data["uuid"],
            name=data["name"],
            product_contents=product_contents,
        )
