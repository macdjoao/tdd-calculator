from src.division import division
from .conftest import valid_numbers, invalid_numbers, invalid_first_number, invalid_second_number
import pytest
from pytest import mark


@mark.division
def test_division_valid_numbers(valid_numbers):
    """test_division
    """
    # When
    result = division(valid_numbers)

    # Then
    assert result == (valid_numbers[0] / valid_numbers[1])


@mark.division
def test_division_invalid_numbers(invalid_numbers):
    """test_division
    """

    # When
    with pytest.raises(Exception):
        result = division(invalid_numbers)

        # Then
        assert result


@mark.division
def test_division_invalid_first_number(invalid_first_number):

    # When
    with pytest.raises(Exception):
        result = division(invalid_first_number)

        # Then
        assert result


@mark.division
def test_division_invalid_second_number(invalid_second_number):

    # When
    with pytest.raises(Exception):
        result = division(invalid_second_number)

        # Then
        assert result


@mark.division
def test_division_by_zero(valid_numbers):

    # When
    with pytest.raises(ZeroDivisionError):
        result = division(valid_numbers[0] / 0)

        # Then
        assert result
