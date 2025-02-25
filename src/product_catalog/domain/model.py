from typing import Sequence
from src.shared.domain.model import Entity
from src.shared.domain.model import ValueObject
from src.service_catalog.domain.model import TechnologyService

class ProductTemplate(Entity):
    def __init__(self, uuid: str, name: str, services: Sequence[TechnologyService]) -> None:
        super().__init__(uuid)
        self.name = name
        self.services = set(services)

    def add_product_content(self, *services: Sequence[TechnologyService]) -> None:
        for service in services:
            self.services.add(service)

    def remove_product_content(self, *services: Sequence[TechnologyService]) -> None:
        for service in services:
            self.services.discard(service)

    def __str__(self) -> str:
        sorted_contents = sorted(self.services, key=lambda x: x.uuid)
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
        self.content_values: dict[str, ValueObject] = {}

    def __str__(self) -> str:
        template_name = self.product_template.name
        value_strings = ", ".join(f"{k}: {v}" for k, v in self.content_values.items())
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"product_template={template_name}, "
            f"content_values=[{value_strings}])"
        )
