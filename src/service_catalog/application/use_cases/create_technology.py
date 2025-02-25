from src.service_catalog.domain.model import Technology
from src.service_catalog.infrastructure.repositories.technology_repository import TechnologyRepository
from src.shared.application.uuid_generator import generate_uuid

class CreateTechnologyUseCase:
    def __init__(self, technology_repository: TechnologyRepository):
        self.technology_repository = technology_repository

    def execute(self, name: str, abbreviation: str = "NA") -> Technology:
        """Creates a technology and adds it to the repository."""
        uuid = generate_uuid(prefix="TECH-")
        technology = Technology(uuid=uuid, name=name, abbreviation=abbreviation)
        self.technology_repository.add(technology)
        return technology
