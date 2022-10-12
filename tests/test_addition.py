from src.addition import addition
from faker import Faker

fake = Faker(locale='en_US')


def test_addition():
    """test_addition
    """

    # Given
    first_entry = fake.random_number()
    second_entry = fake.random_number()
    payload = (first_entry, second_entry)

    # When
    result = addition(payload)

    # Then
    assert result == (first_entry + second_entry)
