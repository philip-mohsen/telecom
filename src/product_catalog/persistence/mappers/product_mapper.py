from src.shared.persistence.mappers.base import JSONMapper
from src.service_catalog.domain.content_value_mapping import CONTENT_VALUE_MAPPING
from src.product_catalog.domain.model import Product
from src.product_catalog.repositories.product_template_repository import ProductTemplateRepository
from src.product_catalog.repositories.product_content_repository import ProductContentRepository

class ProductMapper(JSONMapper[Product]):
    @staticmethod
    def to_dict(product: Product) -> dict:
        content_values_data = {}
        for content_uuid, value_object in product.content_values.items():
            content_values_data[content_uuid] = value_object.value

        return {
            "uuid": product.uuid,
            "name": product.name,
            "product_template": product.product_template.uuid,
            "content_values": content_values_data,
        }

    @staticmethod
    def from_dict(
        data:dict,
        product_template_repository: ProductTemplateRepository,
        product_content_repository: ProductContentRepository
    ) -> Product:
        product_template = product_template_repository.get_by_uuid(data["product_template"])
        content_values = {}

        for content_uuid, value in data["content_values"].items():
            product_content = product_content_repository.get_by_uuid(content_uuid)
            product_content_value_type = product_content.service.content_value_type
            content_values[content_uuid] = CONTENT_VALUE_MAPPING[product_content_value_type](value)

        return Product(
            uuid=data["uuid"],
            name=data["name"],
            product_template=product_template,
            content_values=content_values
        )
