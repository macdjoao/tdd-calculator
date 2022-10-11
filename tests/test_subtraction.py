from operator import sub
from src.subtraction import subtraction
from faker import Faker

fake = Faker(locale='en_US')


def test_subtraction():

    # Given
    first_entry = fake.random_number()
    second_entry = fake.random_number()
    payload = (first_entry, second_entry)

    # When
    result = subtraction(payload)

    # Then
    assert result == (first_entry - second_entry)
