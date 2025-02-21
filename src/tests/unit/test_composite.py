import pytest
from domain.model import Technology
from domain.composites import TechnologyComposite
from exceptions import InvalidEntityComponentTypeError
import hashlib

# Fixtures (for creating instances)
@pytest.fixture
def technology_factory():
    def _create_technology(uuid, name, abbreviation=None):
        return Technology(uuid, name, abbreviation)
    return _create_technology

@pytest.fixture
def technology_composite_factory():
    def _create_technology_composite(name):
        return TechnologyComposite(name)
    return _create_technology_composite

def test_add_technology_component_to_composite(technology_composite_factory, technology_factory):
    """
    Test adding a TechnologyComponent to a TechnologyComposite.
    """
    composite = technology_composite_factory("Composite 1")
    tech = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    composite.add(tech)
    assert tech in composite.members
    assert tech.parent == composite

def test_add_invalid_component_to_composite(technology_composite_factory):
    """
    Test adding an invalid component to a TechnologyComposite.
    """
    composite = technology_composite_factory("Composite 1")
    with pytest.raises(InvalidEntityComponentTypeError):
        composite.add("Invalid Component")  # This should raise an error

def test_composite_uuid(technology_composite_factory, technology_factory):
    """
    Test the UUID generation for a TechnologyComposite.
    """
    composite = technology_composite_factory("Composite 1")
    tech1 = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    tech2 = technology_factory("123e4567-e89b-12d3-a456-426614174001", "LTE")
    composite.add(tech1)
    composite.add(tech2)
    expected_uuid = hashlib.sha256("123e4567-e89b-12d3-a456-426614174000123e4567-e89b-12d3-a456-426614174001".encode()).hexdigest()
    assert composite.uuid == expected_uuid

def test_composite_str_without_abbreviation(technology_composite_factory, technology_factory):
    """
    Test the __str__ method of a TechnologyComposite without abbreviation.
    """
    composite = technology_composite_factory("Composite 1")
    tech1 = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    tech2 = technology_factory("123e4567-e89b-12d3-a456-426614174001", "LTE")
    composite.add(tech1)
    composite.add(tech2)
    expected_str = "TechnologyComposite(name='Composite 1', members=[Technology(name='5G'), Technology(name='LTE')])"
    assert str(composite) == expected_str

def test_composite_str_with_abbreviation(technology_composite_factory, technology_factory):
    """
    Test the __str__ method of a TechnologyComposite with abbreviation.
    """
    composite = technology_composite_factory("Composite 1")
    tech1 = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation")
    tech2 = technology_factory("123e4567-e89b-12d3-a456-426614174001", "LTE", "Long Term Evolution")
    composite.add(tech1)
    composite.add(tech2)
    expected_str = "TechnologyComposite(name='Composite 1', members=[Technology(name='5G', abbreviation='Fifth Generation'), Technology(name='LTE', abbreviation='Long Term Evolution')])"
    assert str(composite) == expected_str

def test_technology_composite_add_invalid_type(technology_composite_factory):
    """
    Test adding an invalid type to a TechnologyComposite.
    """
    composite = technology_composite_factory("Composite 1")
    with pytest.raises(InvalidEntityComponentTypeError):
        composite.add(123)  # This should raise an error

def test_add_composite_to_composite(technology_composite_factory, technology_factory):
    """
    Test adding a TechnologyComposite to another TechnologyComposite.
    """
    parent_composite = technology_composite_factory("Parent Composite")
    child_composite = technology_composite_factory("Child Composite")
    tech = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    child_composite.add(tech)
    parent_composite.add(child_composite)
    assert child_composite in parent_composite.members
    assert child_composite.parent == parent_composite
    assert tech in child_composite.members
    assert tech.parent == child_composite

def test_deep_composite_structure(technology_composite_factory, technology_factory):
    """
    Test a deep composite structure.
    """
    root_composite = technology_composite_factory("Root Composite")
    level1_composite = technology_composite_factory("Level 1 Composite")
    level2_composite = technology_composite_factory("Level 2 Composite")
    tech = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    level2_composite.add(tech)
    level1_composite.add(level2_composite)
    root_composite.add(level1_composite)
    assert level1_composite in root_composite.members
    assert level2_composite in level1_composite.members
    assert tech in level2_composite.members
    assert level1_composite.parent == root_composite
    assert level2_composite.parent == level1_composite
    assert tech.parent == level2_composite

def test_deep_composite_uuid(technology_composite_factory, technology_factory):
    """
    Test the UUID generation for a deep composite structure.
    """
    root_composite = technology_composite_factory("Root Composite")
    level1_composite = technology_composite_factory("Level 1 Composite")
    level2_composite = technology_composite_factory("Level 2 Composite")
    tech1 = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    tech2 = technology_factory("123e4567-e89b-12d3-a456-426614174001", "LTE")
    level2_composite.add(tech1)
    level1_composite.add(level2_composite)
    root_composite.add(level1_composite)
    root_composite.add(tech2)
    expected_uuid_level2 = hashlib.sha256("123e4567-e89b-12d3-a456-426614174000".encode()).hexdigest()
    expected_uuid_level1 = hashlib.sha256(expected_uuid_level2.encode()).hexdigest()
    expected_uuid_root = hashlib.sha256(f"{expected_uuid_level1}123e4567-e89b-12d3-a456-426614174001".encode()).hexdigest()
    assert root_composite.uuid == expected_uuid_root

def test_add_invalid_component_to_deep_composite(technology_composite_factory, technology_factory):
    """
    Test adding an invalid component to a deep composite structure.
    """
    root_composite = technology_composite_factory("Root Composite")
    level1_composite = technology_composite_factory("Level 1 Composite")
    level2_composite = technology_composite_factory("Level 2 Composite")
    tech = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    level2_composite.add(tech)
    level1_composite.add(level2_composite)
    root_composite.add(level1_composite)
    with pytest.raises(InvalidEntityComponentTypeError):
        level2_composite.add("Invalid Component")  # This should raise an error

def test_add_same_component_multiple_times(technology_composite_factory, technology_factory):
    """
    Test adding the same component to a composite multiple times (shouldn't have duplicates).
    """
    composite = technology_composite_factory("Composite 1")
    tech = technology_factory("123e4567-e89b-12d3-a456-426614174000", "5G")
    composite.add(tech)
    composite.add(tech)
    assert len(composite.members) == 1

def test_add_empty_composite_to_composite(technology_composite_factory):
    """
    Test adding an empty composite to another composite.
    """
    parent_composite = technology_composite_factory("Parent Composite")
    empty_composite = technology_composite_factory("Empty Composite")
    parent_composite.add(empty_composite)
    assert empty_composite in parent_composite.members
    assert len(empty_composite.members) == 0

def test_create_composite_with_no_name():
    """
    Test creating a composite with no name.
    """
    with pytest.raises(TypeError):
        TechnologyComposite()
