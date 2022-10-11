from src.get_values import get_values
from faker import Faker

fake = Faker(locale='en_US')


def test_get_values(monkeypatch):

    # Given
    first_entry = fake.random_number()
    second_entry = fake.random_number()

    # When
    inputs = iter([first_entry, second_entry])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_values()

    # Then
    assert result == (first_entry, second_entry)
