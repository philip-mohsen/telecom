from src.shared.repositories.base import Repository
from src.service_catalog.domain.model import TechnologyService
from src.persistance.json_db import JSONDatabase
from src.persistance.json_mappers.technolog_service_mapper import TechnologyServiceMapper
from .technology_repository import TechnologyRepository

class TechnologyServiceRepository(Repository[TechnologyService]):
    def __init__(self, json_db: JSONDatabase):
        self.json_db = json_db
        self.data = self.json_db.load_data("technology_services")
        self.technology_repository = TechnologyRepository(json_db)

    def add(self, technology_service: TechnologyService) -> None:
        self.data[technology_service.uuid] = TechnologyServiceMapper.to_dict(technology_service)
        self.json_db.save_data("technology_services", self.data)

    def get_by_uuid(self, uuid: str) -> TechnologyService:
        data = self.data.get(uuid)
        if data is None:
            raise KeyError(f"TechnologyService with uuid {uuid} not found.")
        return TechnologyServiceMapper.from_dict(data, self.technology_repository)

    def update(self, technology_service: TechnologyService) -> None:
        pass

    def delete(self, uuid: str) -> None:
        pass

    def get_all(self) -> list[TechnologyService]:
        pass
