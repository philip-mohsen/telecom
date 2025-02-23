from typing import Sequence
from src.shared.domain.model import Entity
from src.shared.domain.model import SimpleValueObject
from src.service_catalog.domain.model import TechnologyService

class ProductContent(Entity):
    def __init__(self, uuid: str, name: str, service: TechnologyService):
        super().__init__(uuid)
        self.name = name
        self.service = service

    def __str__(self):
        return f"ProductContent(name={self.name}, service={self.service})"

class ProductTemplate(Entity):
    def __init__(self, uuid: str, name: str, product_contents: Sequence[ProductContent]) -> None:
        super().__init__(uuid)
        self.name = name
        self.product_contents = set(product_contents)

    def add_product_content(self, *product_contents: Sequence[ProductContent]) -> None:
        for product_content in product_contents:
            self.product_contents.add(product_content)

    def remove_product_content(self, *product_contents: Sequence[ProductContent]) -> None:
        for product_content in product_contents:
            self.product_contents.discard(product_content)

    def __str__(self) -> str:
        sorted_contents = sorted(self.product_contents, key=lambda x: x.uuid)
        content_strings = ", ".join(str(content) for content in sorted_contents)
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"product_contents=[{content_strings}])"
        )

class Product(Entity):
    def __init__(self, uuid: str, name: str, product_template: ProductTemplate) -> None:
        super().__init__(uuid)
        self.name = name
        self.product_template = product_template
        self.content_values: dict[str, SimpleValueObject] = {}

    def __str__(self) -> str:
        template_name = self.product_template.name
        value_strings = ", ".join(f"{k}: {v}" for k, v in self.content_values.items())
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"product_template={template_name}, "
            f"content_values=[{value_strings}])"
        )
