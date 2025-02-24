from src.shared.infrastructure.repositories.base import Repository
from src.shared.infrastructure.json_db import JSONDatabase
from src.product_catalog.domain.model import ProductTemplate
from src.product_catalog.infrastructure.mappers.product_template_mapper import ProductTemplateMapper
from src.product_catalog.infrastructure.repositories.product_content_repository import ProductContentRepository

class ProductTemplateRepository(Repository[ProductTemplate]):
    def __init__(self, json_db: JSONDatabase):
        self.json_db = json_db
        self.data = self.json_db.load_data("product_templates")
        self.product_content_repository = ProductContentRepository(json_db=json_db)

    def add(self, product_template: ProductTemplate) -> None:
        self.data[product_template.uuid] = ProductTemplateMapper.to_dict(product_template)
        self.json_db.save_data("product_templates", self.data)

    def get_by_uuid(self, uuid: str) -> ProductTemplate:
        data = self.data.get(uuid)
        if data is None:
            raise KeyError(f"ProductTemplate with uuid {uuid} not found.")
        return ProductTemplateMapper.from_dict(data, self.product_content_repository)

    def get_all(self) -> list[ProductTemplate]:
        pass

    def update(self, product_template: ProductTemplate) -> None:
        pass

    def delete(self, product_template: ProductTemplate) -> None:
        pass
