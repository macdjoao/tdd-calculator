from src.division import division
from faker import Faker

fake = Faker(locale='en_US')


def test_division():

    # Given
    first_entry = fake.random_number()
    second_entry = fake.random_number()
    payload = (first_entry, second_entry)

    # When
    result = division(payload)

    # Then
    assert result == (first_entry / second_entry)
