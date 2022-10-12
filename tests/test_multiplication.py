from src.multiplication import multiplication
from .conftest import valid_numbers, invalid_numbers, invalid_first_number, invalid_second_number
import pytest
from pytest import mark


@mark.multiplication
def test_multiplication_valid_numbers(valid_numbers):
    """test_multiplication
    """
    # When
    result = multiplication(valid_numbers)

    # Then
    assert result == (valid_numbers[0] * valid_numbers[1])


@mark.multiplication
def test_multiplication_invalid_numbers(invalid_numbers):
    """test_multiplication
    """

    # When
    with pytest.raises(Exception):
        result = multiplication(invalid_numbers)

        # Then
        assert result


@mark.multiplication
def test_multiplication_invalid_first_number(invalid_first_number):
    """test_multiplication
    """

    # When
    with pytest.raises(Exception):
        result = multiplication(invalid_numbers)

        # Then
        assert result


@mark.multiplication
def test_multiplication_invalid_second_number(invalid_second_number):
    """test_multiplication
    """

    # When
    with pytest.raises(Exception):
        result = multiplication(invalid_numbers)

        # Then
        assert result
