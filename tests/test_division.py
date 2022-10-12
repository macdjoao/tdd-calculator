from src.division import division
from .fixtures import numbers


def test_division(numbers):
    """test_division
    """
    # When
    result = division(numbers)

    # Then
    assert result == (numbers[0] / numbers[1])
