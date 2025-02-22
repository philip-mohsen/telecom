from src.shared.repositories.base import Repository
from src.service_catalog.domain.model import Technology
from src.persistance.json_db import JSONDatabase
from src.persistance.json_mappers import TechnologyMapper

class TechnologyRepository(Repository[Technology]):
    def __init__(self, json_db: JSONDatabase):
        self.json_db = json_db
        self.data = self.json_db.load_data("technologies")

    def add(self, technology: Technology) -> None:
        self.data[technology.uuid] = TechnologyMapper.to_dict(technology)
        self.json_db.save_data("technologies", self.data)

    def get_by_uuid(self, uuid: str) -> Technology:
        data = self.data.get(uuid)
        if data is None:
            raise KeyError(f"Technology with uuid {uuid} not found.")
        return TechnologyMapper.from_dict(data)
