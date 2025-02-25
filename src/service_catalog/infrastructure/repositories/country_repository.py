from src.shared.infrastructure.repositories.base import Repository
from src.service_catalog.domain.model import Country
from src.shared.infrastructure.json_db import JSONDatabase
from src.service_catalog.infrastructure.mappers.country_mapper import CountryMapper

class CountryRepository(Repository[Country]):
    def __init__(self, json_db: JSONDatabase):
        self.json_db = json_db
        self.data = self.json_db.load_data("countries")

    def add(self, country: Country) -> None:
        self.data[country.uuid] = CountryMapper.to_dict(country)
        self.json_db.save_data("countries", self.data)

    def get_by_uuid(self, uuid: str) -> Country:
        data = self.data.get(uuid)
        if data is None:
            raise KeyError(f"Country with uuid {uuid} not found.")
        return CountryMapper.from_dict(data)

    def update(self, country: Country) -> None:
        pass

    def delete(self, uuid: str) -> None:
        pass

    def get_all(self) -> list[Country]:
        pass
