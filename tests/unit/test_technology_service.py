import pytest
from domain.model import Technology
from domain.services import TechnologyService
from exceptions import MissingRequiredTechnologyError

@pytest.fixture(name="technology_service")
def fixture_technology_service():
    tech1 = Technology(uuid="tech-uuid-1", name="5G", abbreviation="5G")
    tech2 = Technology(uuid="tech-uuid-2", name="4G", abbreviation="4G")
    service = TechnologyService(
        uuid="service-uuid",
        name="Mobile Service",
        technologies=[tech1, tech2])
    return service, tech1, tech2

def test_technology_service_initialization(technology_service):
    service, tech1, tech2 = technology_service
    assert service.uuid == "service-uuid"
    assert service.name == "Mobile Service"
    assert tech1 in service.technologies
    assert tech2 in service.technologies

def test_technology_service_str(technology_service):
    service, _, _ = technology_service
    assert str(service) == "TechnologyService(name='Mobile Service', technologies=[Technology(name='5G', abbreviation='5G'), Technology(name='4G', abbreviation='4G')])"

def test_technology_service_add_technology(technology_service):
    service, _, _ = technology_service
    new_tech = Technology(uuid="tech-uuid-3", name="3G", abbreviation="3G")
    service.add_technology(new_tech)
    assert new_tech in service.technologies

def test_technology_service_remove_technology(technology_service):
    service, tech1, _ = technology_service
    service.remove_technology(tech1)
    assert tech1 not in service.technologies

def test_technology_service_remove_all_technologies():
    tech1 = Technology(uuid="tech-uuid-1", name="5G", abbreviation="5G")
    service = TechnologyService(uuid="service-uuid", name="Mobile Service", technologies=[tech1])
    with pytest.raises(MissingRequiredTechnologyError):
        service.remove_technology(tech1) # This should raise an error

def test_technology_service_duplicate_technology(technology_service):
    service, _, _ = technology_service
    duplicate_tech = Technology(uuid="tech-uuid-1", name="5G", abbreviation="5G")
    service.add_technology(duplicate_tech)
    assert len(service.technologies) == 2  # No duplicates should be added
