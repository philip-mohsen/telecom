"""
Unit tests for the composite module.
"""

import hashlib
import pytest
from domain.model import Technology
from domain.composites import TechnologyComposite
from exceptions import InvalidEntityComponentTypeError

# Fixtures (for creating instances)
@pytest.fixture(name="technology_factory_fixture")
def technology_factory():
    """
    Fixture for creating a technology factory.
    """
    def _create_technology(uuid, name, abbreviation=None):
        return Technology(uuid, name, abbreviation)
    return _create_technology

@pytest.fixture(name="technology_composite_factory_fixture")
def technology_composite_factory():
    """
    Fixture for creating a technology composite factory.
    """
    def _create_technology_composite(name):
        return TechnologyComposite(name)
    return _create_technology_composite

def test_add_technology_component_to_composite(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test adding a TechnologyComponent to a TechnologyComposite.
    """
    composite = technology_composite_factory_fixture("Composite 1")
    tech = technology_factory_fixture("uuid1", "5G")
    composite.add(tech)
    assert tech in composite.members
    assert tech.parent == composite

def test_add_invalid_component_to_composite(technology_composite_factory_fixture):
    """
    Test adding an invalid component to a TechnologyComposite.
    """
    composite = technology_composite_factory_fixture("Composite 1")
    with pytest.raises(InvalidEntityComponentTypeError):
        composite.add("Invalid Component")  # This should raise an error

def test_composite_uuid(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test the UUID generation for a TechnologyComposite.
    """
    composite = technology_composite_factory_fixture("Composite 1")
    tech1 = technology_factory_fixture("uuid1", "5G")
    tech2 = technology_factory_fixture("uuid2", "LTE")
    composite.add(tech1)
    composite.add(tech2)
    expected_uuid = hashlib.sha256("uuid1uuid2".encode()).hexdigest()
    assert composite.uuid == expected_uuid

def test_composite_str_without_abbreviation(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test the __str__ method of a TechnologyComposite without abbreviation.
    """
    composite = technology_composite_factory_fixture("Composite 1")
    tech1 = technology_factory_fixture("uuid1", "5G")
    tech2 = technology_factory_fixture("uuid2", "LTE")
    composite.add(tech1)
    composite.add(tech2)
    expected_str = "TechnologyComposite(name='Composite 1', members=[Technology(name='5G'), Technology(name='LTE')])"
    assert str(composite) == expected_str

def test_composite_str_with_abbreviation(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test the __str__ method of a TechnologyComposite with abbreviation.
    """
    composite = technology_composite_factory_fixture("Composite 1")
    tech1 = technology_factory_fixture("uuid1", "5G", "Fifth Generation")
    tech2 = technology_factory_fixture("uuid2", "LTE", "Long Term Evolution")
    composite.add(tech1)
    composite.add(tech2)
    expected_str = "TechnologyComposite(name='Composite 1', members=[Technology(name='5G', abbreviation='Fifth Generation'), Technology(name='LTE', abbreviation='Long Term Evolution')])"
    assert str(composite) == expected_str

def test_technology_composite_add_invalid_type(technology_composite_factory_fixture):
    """
    Test adding an invalid type to a TechnologyComposite.
    """
    composite = technology_composite_factory_fixture("Composite 1")
    with pytest.raises(InvalidEntityComponentTypeError):
        composite.add(123)  # This should raise an error

def test_add_composite_to_composite(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test adding a TechnologyComposite to another TechnologyComposite.
    """
    parent_composite = technology_composite_factory_fixture("Parent Composite")
    child_composite = technology_composite_factory_fixture("Child Composite")
    tech = technology_factory_fixture("uuid1", "5G")
    child_composite.add(tech)
    parent_composite.add(child_composite)
    assert child_composite in parent_composite.members
    assert child_composite.parent == parent_composite
    assert tech in child_composite.members
    assert tech.parent == child_composite

def test_deep_composite_structure(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test a deep composite structure.
    """
    root_composite = technology_composite_factory_fixture("Root Composite")
    level1_composite = technology_composite_factory_fixture("Level 1 Composite")
    level2_composite = technology_composite_factory_fixture("Level 2 Composite")
    tech = technology_factory_fixture("uuid1", "5G")
    level2_composite.add(tech)
    level1_composite.add(level2_composite)
    root_composite.add(level1_composite)
    assert level1_composite in root_composite.members
    assert level2_composite in level1_composite.members
    assert tech in level2_composite.members
    assert level1_composite.parent == root_composite
    assert level2_composite.parent == level1_composite
    assert tech.parent == level2_composite

def test_deep_composite_uuid(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test the UUID generation for a deep composite structure.
    """
    root_composite = technology_composite_factory_fixture("Root Composite")
    level1_composite = technology_composite_factory_fixture("Level 1 Composite")
    level2_composite = technology_composite_factory_fixture("Level 2 Composite")
    tech1 = technology_factory_fixture("uuid1", "5G")
    tech2 = technology_factory_fixture("uuid2", "LTE")
    level2_composite.add(tech1)
    level1_composite.add(level2_composite)
    root_composite.add(level1_composite)
    root_composite.add(tech2)
    expected_uuid_level2 = hashlib.sha256("uuid1".encode()).hexdigest()
    expected_uuid_level1 = hashlib.sha256(expected_uuid_level2.encode()).hexdigest()
    expected_uuid_root = hashlib.sha256(f"{expected_uuid_level1}uuid2".encode()).hexdigest()
    assert root_composite.uuid == expected_uuid_root

def test_add_invalid_component_to_deep_composite(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test adding an invalid component to a deep composite structure.
    """
    root_composite = technology_composite_factory_fixture("Root Composite")
    level1_composite = technology_composite_factory_fixture("Level 1 Composite")
    level2_composite = technology_composite_factory_fixture("Level 2 Composite")
    tech = technology_factory_fixture("uuid1", "5G")
    level2_composite.add(tech)
    level1_composite.add(level2_composite)
    root_composite.add(level1_composite)
    with pytest.raises(InvalidEntityComponentTypeError):
        level2_composite.add("Invalid Component")  # This should raise an error

def test_add_same_component_multiple_times(technology_composite_factory_fixture, technology_factory_fixture):
    """
    Test adding the same component to a composite multiple times (shouldn't have duplicates).
    """
    composite = technology_composite_factory_fixture("Composite 1")
    tech = technology_factory_fixture("uuid1", "5G")
    composite.add(tech)
    composite.add(tech)
    assert len(composite.members) == 1

def test_create_composite_with_no_name():
    """
    Test creating a composite with no name.
    """
    with pytest.raises(TypeError):
        TechnologyComposite()
