from src.shared.infrastructure.mappers.base import JSONMapper
from src.service_catalog.domain.value_objects import MinuteValue, DataLimitValue, ChannelValue
from src.service_catalog.infrastructure.mappers.minute_value_mapper import MinuteValueMapper
from src.service_catalog.infrastructure.mappers.data_limit_value_mapper import DataLimitValueMapper
from src.service_catalog.infrastructure.mappers.channel_value_mapper import ChannelValueMapper
from src.service_catalog.infrastructure.repositories.technology_service_repository import TechnologyServiceRepository
from src.service_catalog.domain.content_value_mapping import CONTENT_VALUE_MAPPING
from src.product_catalog.domain.model import Product
from src.product_catalog.infrastructure.repositories.product_template_repository import ProductTemplateRepository

VALUE_OBJECT_MAPPERS = {
    MinuteValue: MinuteValueMapper,
    DataLimitValue: DataLimitValueMapper,
    ChannelValue: ChannelValueMapper,
}

class ProductMapper(JSONMapper[Product]):
    @staticmethod
    def to_dict(product: Product) -> dict:
        content_values_data = {}
        for service_uuid, value_object in product.content_values.items():
            mapper = VALUE_OBJECT_MAPPERS.get(type(value_object))
            content_values_data[service_uuid] = mapper.to_dict(value_object)

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
        service_technology_repository: TechnologyServiceRepository
    ) -> Product:
        product_template = product_template_repository.get_by_uuid(data["product_template"])
        content_values = {}

        for service_uuid, values in data["content_values"].items():
            service = service_technology_repository.get_by_uuid(service_uuid)
            service_content_value_type = service.content_value_type
            mapper = CONTENT_VALUE_MAPPING[service_content_value_type]
            content_values[service_uuid] = mapper(**values)

        return Product(
            uuid=data["uuid"],
            name=data["name"],
            product_template=product_template,
            content_values=content_values
        )
