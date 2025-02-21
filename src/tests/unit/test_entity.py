import pytest
from domain.model import Entity

@pytest.mark.parametrize("uuid1, uuid2, expected", [
    ("123e4567-e89b-12d3-a456-426614174000", "123e4567-e89b-12d3-a456-426614174000", True),
    ("123e4567-e89b-12d3-a456-426614174000", "123e4567-e89b-12d3-a456-426614174001", False),
    ("123e4567-e89b-12d3-a456-426614174000", 123, False),
    ("123e4567-e89b-12d3-a456-426614174000", None, False),
])
def test_entity_equality(uuid1, uuid2, expected):
    """
    Test the equality operator for the Entity class.
    """
    entity1 = Entity(uuid1)
    entity2 = Entity(uuid2)
    assert (entity1 == entity2) == expected

@pytest.mark.parametrize("uuid1, uuid2, expected", [
    ("123e4567-e89b-12d3-a456-426614174001", "123e4567-e89b-12d3-a456-426614174000", True),
    ("123e4567-e89b-12d3-a456-426614174000", 123, True),
    ("123e4567-e89b-12d3-a456-426614174000", None, True),
])
def test_entity_inequality(uuid1, uuid2, expected):
    """
    Test the inequality operator for the Entity class.
    """
    entity1 = Entity(uuid1)
    entity2 = Entity(uuid2)
    assert (entity1 != entity2) == expected

@pytest.mark.parametrize("uuid, expected_hash", [
    ("123e4567-e89b-12d3-a456-426614174000", hash("123e4567-e89b-12d3-a456-426614174000")),
    ("123e4567-e89b-12d3-a456-426614174001", hash("123e4567-e89b-12d3-a456-426614174001")),
])
def test_entity_hash(uuid, expected_hash):
    """
    Test the hash function for the Entity class.
    """
    entity = Entity(uuid)
    assert hash(entity) == expected_hash

@pytest.mark.parametrize("uuid, expected_str", [
    ("123e4567-e89b-12d3-a456-426614174000", "Entity(uuid='123e4567-e89b-12d3-a456-426614174000')"),
    ("123e4567-e89b-12d3-a456-426614174001", "Entity(uuid='123e4567-e89b-12d3-a456-426614174001')"),
])
def test_entity_str(uuid, expected_str):
    """
    Test the string representation of the Entity class.
    """
    entity = Entity(uuid)
    assert str(entity) == expected_str

@pytest.mark.parametrize("invalid_uuid", [
    (123),
    (None),
    ("invalid-uuid"),
])
def test_entity_invalid_uuid(invalid_uuid):
    """
    Test the Entity class with invalid UUIDs.
    """
    with pytest.raises(ValueError):
        Entity(invalid_uuid)
