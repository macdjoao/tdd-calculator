from src.subtraction import subtraction
from .conftest import valid_numbers, invalid_numbers, invalid_first_number, invalid_second_number
import pytest


def test_subtraction_valid_numbers(valid_numbers):
    """test_subtraction
    """
    # When
    result = subtraction(valid_numbers)

    # Then
    assert result == (valid_numbers[0] - valid_numbers[1])


def test_subtraction_invalid_numbers(invalid_numbers):
    """test_subtraction
    """

    # When
    with pytest.raises(Exception):
        result = subtraction(invalid_numbers)

        # Then
        assert result


def test_subtraction_invalid_first_number(invalid_first_number):

    # When
    with pytest.raises(Exception):
        result = subtraction(invalid_first_number)

        # Then
        assert result


def test_subtraction_invalid_second_number(invalid_second_number):

    # When
    with pytest.raises(Exception):
        result = subtraction(invalid_second_number)

        # Then
        assert result
