from src.subtraction import subtraction
from .fixtures import numbers


def test_subtraction(numbers):
    """test_subtraction
    """
    # When
    result = subtraction(numbers)

    # Then
    assert result == (numbers[0] - numbers[1])
