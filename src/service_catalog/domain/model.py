from __future__ import annotations
from typing import Sequence
from src.exceptions import MissingRequiredTechnologyError
from src.shared.domain.model import Entity
from src.service_catalog.domain.enums import ContentValueType
from src.service_catalog.domain.value_objects import Country

class Technology(Entity):
    def __init__(self, uuid: str, name: str, abbreviation: str = "NA") -> None:
        super().__init__(uuid)
        self.name = name
        self.abbreviation = abbreviation

    def __str__(self) -> str:
        if self.abbreviation:
            return (
                f"{self.__class__.__name__}(name={self.name}, "
                f"abbreviation={self.abbreviation})"
            )
        return f"{self.__class__.__name__}(name={self.name})"

class TechnologyService(Entity):
    def __init__(self, uuid: str, name: str, technologies: Sequence[Technology], content_value_type: ContentValueType) -> None:
        super().__init__(uuid)
        self.name = name
        self.technologies = set(technologies)
        self.content_value_type = content_value_type
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
        return (
            f"{self.__class__.__name__}(name={self.name}, "
            f"technologies=[{technology_strings}]), "
            f"content_value_type={self.content_value_type})"
        )

class Country(Entity):
    def __init__(self, uuid: str, name: str) -> None:
        super().__init__(uuid)
        self.name = name

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"

class CountryZone(Entity):
    def __init__(self, uuid: str, name: str, countries: Sequence[Country]) -> None:
        super().__init__(uuid)
        self.name = name
        self.countries = set(countries)

    def add_country(self, *countries: Sequence[Country]) -> None:
        for country in countries:
            self.countries.add(country)

    def remove_country(self, *countries: Sequence[Country]) -> None:
        for country in countries:
            self.countries.discard(country)

    def __str__(self) -> str:
        sorted_countries = sorted(self.countries, key=lambda x: x.value)
        country_strings = ", ".join(str(country) for country in sorted_countries)
        return (
            f"{self.__class__.__name__}(name={self.name}, "
            f"countries=[{country_strings}])"
        )

class Channel(Entity):
    def __init__(self, uuid: str, name: str) -> None:
        super().__init__(uuid)
        self.name = name

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"

class TVPackage(Entity):
    def __init__(self, uuid: str, name: str, channels: Sequence[Channel]) -> None:
        super().__init__(uuid)
        self.name = name
        self.channels = set(channels)

    def add_channel(self, *channels: Sequence[Channel]) -> None:
        for channel in channels:
            self.channels.add(channel)

    def remove_channel(self, *channels: Sequence[Channel]) -> None:
        for channel in channels:
            self.channels.discard(channel)

    def __str__(self) -> str:
        sorted_channels = sorted(self.channels, key=lambda x: x.value)
        channel_strings = ", ".join(str(channel) for channel in sorted_channels)
        return (
            f"{self.__class__.__name__}(name={self.name}, "
            f"channels=[{channel_strings}])"
        )
