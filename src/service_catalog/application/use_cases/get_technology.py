from src.service_catalog.domain.model import Technology
from src.service_catalog.infrastructure.repositories.technology_repository import TechnologyRepository

class GetTechnologyUseCase:
    def __init__(self, technology_repository: TechnologyRepository):
        self.technology_repository = technology_repository

    def execute(self, uuid: str) -> Technology:
        technology = self.technology_repository.get_by_uuid(uuid)
        return technology
