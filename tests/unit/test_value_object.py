import pytest
from domain.model import ValueObject

class MockValueObject(ValueObject):
    def __init__(self, value):
        self.value = value

    def _equal_values(self, other: ValueObject) -> bool:
        return self.value == other.value

    def _hash_values(self) -> int:
        return hash(self.value)

@pytest.fixture(name="value_object_factory_fixture")
def value_object_factory():
    """
    Fixture to create instances of MockValueObject.
    """
    def _create_value_object(value):
        return MockValueObject(value)
    return _create_value_object

@pytest.mark.parametrize("val1, val2, expected", [
    (10, 10, True),
    (10, 20, False),
    ("abc", "abc", True),
    ("abc", "def", False),
    (None, None, True),
    (None, 10, False),
    ((1, 2), (1, 2), True),
    ((1, 2), (2, 1), False),
    (10.5, 10.5, True),
    (10.5, 20.5, False),
])
def test_value_object_equality(value_object_factory_fixture, val1, val2, expected):
    """
    Test the equality of ValueObject instances.
    """
    vo1 = value_object_factory_fixture(val1)
    vo2 = value_object_factory_fixture(val2)
    assert (vo1 == vo2) == expected

@pytest.mark.parametrize("val1, val2, expected", [
    (10, 10, True),
    (10, 20, False),
    ("abc", "abc", True),
    ("abc", "def", False),
    (None, None, True),
    (None, 10, False),
    ((1, 2), (1, 2), True),
    ((1, 2), (2, 1), False),
    (10.5, 10.5, True),
    (10.5, 20.5, False),
])
def test_value_object_hash(value_object_factory_fixture, val1, val2, expected):
    """
    Test the hash values of ValueObject instances.
    """
    vo1 = value_object_factory_fixture(val1)
    vo2 = value_object_factory_fixture(val2)
    assert (hash(vo1) == hash(vo2)) == expected

@pytest.mark.parametrize("val1, val2, expected", [
    (10, 20, True),
    ("abc", "def", True),
    (None, 10, True),
    ((1, 2), (2, 1), True),
    (10.5, 20.5, True),
])
def test_value_object_inequality(value_object_factory_fixture, val1, val2, expected):
    """
    Test the inequality of ValueObject instances.
    """
    vo1 = value_object_factory_fixture(val1)
    vo2 = value_object_factory_fixture(val2)
    assert (vo1 != vo2) == expected
