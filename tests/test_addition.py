from src.addition import addition
from .conftest import valid_numbers, invalid_numbers, invalid_first_number, invalid_second_number
import pytest


def test_addition_valid_numbers(valid_numbers):
    """test_addition
    """
    # When
    result = addition(valid_numbers)

    # Then
    assert result == (valid_numbers[0] + valid_numbers[1])


def test_addition_invalid_numbers(invalid_numbers):
    """test_addition
    """

    # When
    with pytest.raises(Exception):
        result = addition(invalid_numbers)

        # Then
        assert result


def test_addition_invalid_first_number(invalid_first_number):

    # When
    with pytest.raises(Exception):
        result = addition(invalid_first_number)

        # Then
        assert result


def test_addition_invalid_second_number(invalid_second_number):

    # When
    with pytest.raises(Exception):
        result = addition(invalid_second_number)

        # Then
        assert result
