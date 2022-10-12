from src.addition import addition
from .conftest import numbers


def test_addition(numbers):
    """test_addition
    """
    # When
    result = addition(numbers)

    # Then
    assert result == (numbers[0] + numbers[1])
