"""
Mappers for domain object (for JSON persistance demo).
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from src.service_catalog.domain.model import Technology
from src.service_catalog.domain.model import TechnologyEnabledService
from src.service_catalog.repositories.technology_repository import TechnologyRepository

ObjectT = TypeVar("ObjectT")

class JSONMapper(ABC, Generic[ObjectT]):
    """Abstract class for JSON mappers."""

    @staticmethod
    @abstractmethod
    def to_dict(obj: ObjectT) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_dict(self, data: dict) -> ObjectT:
        pass

class TechnologyMapper(JSONMapper[Technology]):
    """Mapper for Technology domain object."""
    @staticmethod
    def to_dict(obj: Technology) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
            "abbreviation": obj.abbreviation,
        }

    @staticmethod
    def from_dict(data: dict) -> Technology:
        return Technology(
            uuid=data["uuid"],
            name=data["name"],
            abbreviation=data["abbreviation"],
        )

class TechnologyEnabledServiceMapper(JSONMapper[TechnologyEnabledService]):
    """Mapper for TechnologyEnabledService domain object."""
    @staticmethod
    def to_dict(obj: TechnologyEnabledService) -> dict:
        return {
            "uuid": obj.uuid,
            "name": obj.name,
            "technologies": [tech.uuid for tech in obj.technologies],
        }

    @staticmethod
    def from_dict(data: dict, technology_repository: TechnologyRepository) -> TechnologyEnabledService:
        return TechnologyEnabledService(
            uuid=data["uuid"],
            name=data["name"],
            technologies=[technology_repository.get_by_uuid(uuid) for uuid in data["technologies"]],
        )
