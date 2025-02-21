import pytest
from domain.model import Entity

class MockEntity(Entity):
    def __str__(self) -> str:
        return f"MockEntity(uuid='{self.uuid}')"

@pytest.mark.parametrize("uuid1, uuid2, expected", [
    ("uuid1", "uuid1", True),
    ("uuid1", "uuid2", False),
    ("uuid1", 123, False),
    ("uuid1", None, False),
])
def test_entity_equality(uuid1, uuid2, expected):
    """
    Test the equality operator for the MockEntity class.
    """
    entity1 = MockEntity(uuid1)
    entity2 = MockEntity(uuid2)
    assert (entity1 == entity2) == expected

@pytest.mark.parametrize("uuid1, uuid2, expected", [
    ("uuid2", "uuid1", True),
    ("uuid1", 123, True),
    ("uuid1", None, True),
])
def test_entity_inequality(uuid1, uuid2, expected):
    """
    Test the inequality operator for the MockEntity class.
    """
    entity1 = MockEntity(uuid1)
    entity2 = MockEntity(uuid2)
    assert (entity1 != entity2) == expected

@pytest.mark.parametrize("uuid, expected_hash", [
    ("uuid1", hash("uuid1")),
    ("uuid2", hash("uuid2")),
])
def test_entity_hash(uuid, expected_hash):
    """
    Test the hash function for the MockEntity class.
    """
    entity = MockEntity(uuid)
    assert hash(entity) == expected_hash
