from src.get_values import get_values
from .conftest import numbers


def test_get_values(monkeypatch, numbers):
    """test_get_values

    Args:
        monkeypatch (string): method to make it possible to read the inputs (provides by Faker) by the function
    """
    # When
    inputs = iter([numbers[0], numbers[1]])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_values()

    # Then
    assert result == (numbers[0], numbers[1])
