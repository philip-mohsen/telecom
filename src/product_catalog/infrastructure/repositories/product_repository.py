from src.shared.infrastructure.repositories.base import Repository
from src.shared.infrastructure.json_db import JSONDatabase
from src.product_catalog.domain.model import Product
from src.product_catalog.infrastructure.mappers.product_mapper import ProductMapper
from src.product_catalog.infrastructure.repositories.product_template_repository import ProductTemplateRepository
from src.product_catalog.infrastructure.repositories.product_content_repository import ProductContentRepository

class ProductRepository(Repository[Product]):
    def __init__(self, json_db: JSONDatabase) -> None:

        self.json_db = json_db
        self.data = self.json_db.load_data("products")
        self.product_template_repository = ProductTemplateRepository(json_db=json_db)
        self.product_content_repository = ProductContentRepository(json_db=json_db)

    def add(self, product: Product) -> None:
        self.data[product.uuid] = ProductMapper.to_dict(product)
        self.json_db.save_data("products", self.data)

    def get_by_uuid(self, uuid: str) -> Product:
        data = self.data.get(uuid)
        if data is None:
            raise KeyError(f"Product with uuid {uuid} not found.")
        return ProductMapper.from_dict(data, self.product_template_repository, self.product_content_repository)

    def get_all(self) -> list[Product]:
        pass

    def update(self, product: Product) -> None:
        pass

    def delete(self, product: Product) -> None:
        pass
