from src.service_catalog.domain.model import TechnologyService
from src.service_catalog.domain.enums import ContentValueType
from src.service_catalog.infrastructure.repositories.technology_repository import TechnologyRepository
from src.service_catalog.infrastructure.repositories.technology_service_repository import TechnologyServiceRepository
from src.shared.application.uuid_generator import generate_uuid

class CreateTechnologyServiceUseCase:
    def __init__(self, technology_repository: TechnologyRepository, technology_service_repository: TechnologyServiceRepository):
        self.technology_repo = technology_repository
        self.technology_service_repo = technology_service_repository

    def execute(self, name: str, technology_uuids: list[str], content_value_type: ContentValueType) -> TechnologyService:
        """Creates a new technology service."""
        technologies = [self.technology_repo.get_by_uuid(uuid) for uuid in technology_uuids]
        uuid = generate_uuid(prefix="TECH-SVC-")
        technology_service = TechnologyService(
            uuid=uuid,
            name=name,
            technologies=technologies,
            content_value_type=content_value_type)

        self.technology_service_repo.add(technology_service)
        return technology_service
