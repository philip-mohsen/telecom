from __future__ import annotations
from typing import Sequence
from exceptions import MissingRequiredTechnologyError
from src.shared.domain.model import Entity

class Technology(Entity):
    def __init__(self, uuid: str, name: str, abbreviation: str = "NA") -> None:
        super().__init__(uuid)
        self.name = name
        self.abbreviation = abbreviation

    def __str__(self) -> str:
        if self.abbreviation:
            return (
                f"{self.__class__.__name__}(name='{self.name}', "
                f"abbreviation='{self.abbreviation}')"
            )
        return f"{self.__class__.__name__}(name='{self.name}')"

class TechnologyEnabledService(Entity):
    def __init__(self, uuid: str, name: str, technologies: Sequence[Technology]) -> None:
        super().__init__(uuid)
        self.name = name
        self.technologies = set(technologies)
        self.validate()

    def validate(self) -> None:
        """Validates that the service has at least one associated technology."""
        if not self.technologies:
            raise MissingRequiredTechnologyError()

    def add_technology(self, *technologies: Sequence[Technology]) -> None:
        for technology in technologies:
            self.technologies.add(technology)

    def remove_technology(self, *technologies: Sequence[Technology]) -> None:
        for technology in technologies:
            self.technologies.discard(technology)
            self.validate()

    def __str__(self) -> str:
        sorted_technologies = sorted(self.technologies, key=lambda x: x.uuid)
        technology_strings = ", ".join(str(tech) for tech in sorted_technologies)
        return f"{self.__class__.__name__}(name='{self.name}', technologies=[{technology_strings}])"
