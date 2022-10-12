from faker import Faker
import pytest

fake = Faker(locale='en_US')

# Given


@pytest.fixture(scope="module")
def numbers():
    """numbers

    Returns:
        tuple: returns a tuple with two random numbers for use in test functions
    """
    first_entry = fake.random_number()
    second_entry = fake.random_number()
    payload = (first_entry, second_entry)
    return payload
