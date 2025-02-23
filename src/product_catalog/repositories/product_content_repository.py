from src.shared.repositories.base import Repository
from src.shared.persistence.json_db import JSONDatabase
from src.service_catalog.repositories.technology_service_repository import TechnologyServiceRepository
from src.product_catalog.domain.model import ProductContent
from src.product_catalog.persistence.mappers.product_content_mapper import ProductContentMapper

class ProductContentRepository(Repository[ProductContent]):
    """Repository for ProductContent domain objects."""
    def __init__(self, json_db: JSONDatabase) -> None:
        self.json_db = json_db
        self.data = self.json_db.load_data("product_contents")
        self.technology_service_repository = TechnologyServiceRepository(json_db)

    def add(self, product_content: ProductContent) -> None:
        self.data[product_content.uuid] = ProductContentMapper.to_dict(product_content)
        self.json_db.save_data("product_contents", self.data)

    def get_by_uuid(self, uuid: str) -> ProductContent:
        data = self.data.get(uuid)
        if data is None:
            raise KeyError(f"ProductContent with uuid {uuid} not found.")
        return ProductContentMapper.from_dict(data, self.technology_service_repository)

    def get_all(self) -> list[ProductContent]:
        pass

    def update(self, product_content: ProductContent) -> None:
        pass

    def delete(self, product_content: ProductContent) -> None:
        pass
