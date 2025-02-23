from src.service_catalog.domain.model import TechnologyService
from src.service_catalog.repositories.technology_repository import TechnologyRepository
from src.service_catalog.repositories.technology_service_repository import TechnologyServiceRepository
from src.shared.application.uuid_generator import generate_uuid

class CreateTechnologyServiceUseCase:
    def __init__(self, technology_repository: TechnologyRepository, technology_service_repository: TechnologyServiceRepository):
        self.technology_repo = technology_repository
        self.technology_service_repo = technology_service_repository

    def execute(self, name: str, technology_uuids: list[str]) -> TechnologyService:
        """Creates a new technology service."""
        technologies = [self.technology_repo.get_by_uuid(uuid) for uuid in technology_uuids]
        uuid = generate_uuid(prefix="TECH-SVC-")
        technology_service = TechnologyService(uuid=uuid, name=name, technologies=technologies)
        self.technology_service_repo.add(technology_service)
        return technology_service
