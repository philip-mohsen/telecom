from src.service_catalog.domain.model import TechnologyService
from src.service_catalog.repositories.technology_service_repository import TechnologyServiceRepository

class GetTechnologyServiceUseCase:
    def __init__(self, technology_service_repository: TechnologyServiceRepository):
        self.technology_service_repository = technology_service_repository

    def execute(self, uuid: str) -> TechnologyService:
        """Retrieves a technology service by its UUID."""
        return self.technology_service_repository.get_by_uuid(uuid)
