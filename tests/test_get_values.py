from src.get_values import get_values
from .conftest import valid_numbers, invalid_numbers, invalid_first_number, invalid_second_number
from pytest import mark


@mark.get_values
def test_get_values(monkeypatch, valid_numbers):
    """test_get_values

    Args:
        monkeypatch (string): method to make it possible to read the inputs (provides by Faker) by the function
    """
    # When
    inputs = iter([valid_numbers[0], valid_numbers[1]])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_values()

    # Then
    assert result == (valid_numbers[0], valid_numbers[1])
