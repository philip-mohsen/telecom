import pytest
from domain.model import Technology

@pytest.mark.parametrize("uuid, name, abbreviation, expected_str", [
    ("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", "Technology(name='5G', abbreviation='Fifth Generation')"),
    ("123e4567-e89b-12d3-a456-426614174001", "LTE", None, "Technology(name='LTE')"),
])
def test_technology_str(uuid, name, abbreviation, expected_str):
    """
    Test the __str__ method of the Technology class.
    """
    tech = Technology(uuid, name, abbreviation)
    assert str(tech) == expected_str

@pytest.mark.parametrize("uuid1, name1, abbreviation1, uuid2, name2, abbreviation2, expected", [
    ("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", "123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", True),
    ("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", "123e4567-e89b-12d3-a456-426614174001", "LTE", None, False),
    ("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", "123e4567-e89b-12d3-a456-426614174001", "5G", "Fifth Generation", False),
])
def test_technology_equality(uuid1, name1, abbreviation1, uuid2, name2, abbreviation2, expected):
    """
    Test the equality operator for the Technology class.
    """
    tech1 = Technology(uuid1, name1, abbreviation1)
    tech2 = Technology(uuid2, name2, abbreviation2)
    assert (tech1 == tech2) == expected

@pytest.mark.parametrize("uuid1, name1, abbreviation1, uuid2, name2, abbreviation2, expected", [
    ("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", "123e4567-e89b-12d3-a456-426614174001", "LTE", None, True),
    ("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", "123e4567-e89b-12d3-a456-426614174001", "5G", "Fifth Generation", True),
])
def test_technology_inequality(uuid1, name1, abbreviation1, uuid2, name2, abbreviation2, expected):
    """
    Test the inequality operator for the Technology class.
    """
    tech1 = Technology(uuid1, name1, abbreviation1)
    tech2 = Technology(uuid2, name2, abbreviation2)
    assert (tech1 != tech2) == expected

@pytest.mark.parametrize("uuid, name, abbreviation, expected_hash", [
    ("123e4567-e89b-12d3-a456-426614174000", "5G", "Fifth Generation", hash("123e4567-e89b-12d3-a456-426614174000")),
    ("123e4567-e89b-12d3-a456-426614174001", "LTE", None, hash("123e4567-e89b-12d3-a456-426614174001")),
])
def test_technology_hash(uuid, name, abbreviation, expected_hash):
    """
    Test the hash function for the Technology class.
    """
    tech = Technology(uuid, name, abbreviation)
    assert hash(tech) == expected_hash