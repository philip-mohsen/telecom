from src.service_catalog.domain.model import Country
from src.service_catalog.infrastructure.repositories.country_repository import CountryRepository
from src.shared.application.uuid_generator import generate_uuid

class CreateCountryUseCase:
    def __init__(self, country_repository: CountryRepository):
        self.country_repository = country_repository

    def execute(self, name: str) -> Country:
        """Create a new country and add it to the repository."""
        uuid = generate_uuid("COUNTRY-")
        country = Country(uuid=uuid, name=name)
        self.country_repository.add(country)
        return country
