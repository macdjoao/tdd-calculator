from faker import Faker
import pytest
import random

fake = Faker(locale='en_US')

# Given


@pytest.fixture(scope="module")
def valid_numbers():
    """numbers

    Returns:
        tuple: returns a tuple with two random numbers for use in test functions
    """
    first_entry = fake.random_number()
    second_entry = fake.random_number()
    payload = (first_entry, second_entry)
    return payload


@pytest.fixture(scope="module")
def invalid_numbers():
    """invalid_numbers

    Returns:
        tuple: returns a tuple with a invalid numbers
    """
    first_entry = random.sample(['abc', ' '], 1)
    second_entry = random.sample(['abc', ' '], 1)
    payload = (first_entry, second_entry)
    return payload


@pytest.fixture(scope="module")
def invalid_first_number():
    """invalid_first_number

    Returns:
        tuple: returns a tuple with a invalid first number
    """
    first_entry = random.sample(['abc', ' '], 1)
    second_entry = fake.random_number()
    payload = (first_entry, second_entry)
    return payload


@pytest.fixture(scope="module")
def invalid_second_number():
    """invalid_second_number

    Returns:
        tuple: returns a tuple with a invalid second number
    """
    first_entry = fake.random_number()
    second_entry = random.sample(['abc', ' '], 1)
    payload = (first_entry, second_entry)
    return payload
