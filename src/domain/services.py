from typing import Sequence
from exceptions import MissingRequiredTechnologyError
from .model import Service
from .model import Technology

class TechnologyService(Service):
    def __init__(self, uuid: str, name: str, technologies: Sequence[Technology]) -> None:
        super().__init__(uuid, name)
        self.technologies = set(technologies)
        self.validate()

    def validate(self) -> None:
        """Validates that the service has at least one associated technology."""
        if not self.technologies:
            raise MissingRequiredTechnologyError()

    def add_technology(self, *technologies: Sequence[Technology]) -> None:
        for technology in technologies:
            self.technologies.add(technology)
            technology.services.add(self)

    def remove_technology(self, *technologies: Sequence[Technology]) -> None:
        for technology in technologies:
            self.technologies.discard(technology)
            technology.services.discard(self)
            self.validate()

    def __str__(self) -> str:
        sorted_technologies = sorted(self.technologies, key=lambda x: x.uuid)
        technology_strings = ", ".join(str(tech) for tech in sorted_technologies)
        return f"{self.__class__.__name__}(name='{self.name}', technologies=[{technology_strings}])"
