def get_values():
    """get_values

    Args:
        first_value (string): first value captured
        second_value (string): second value captured

    Returns:
        int: should return both values as integers
    """
    try:
        first_value = float(input('Type the first number: '))
        second_value = float(input('Type the second number: '))
        return first_value, second_value
    except ValueError as err:
        print(
            f'You must give a two numbers (int or float) for the function: [{err}]')


def addition():
    pass


def subtraction():
    pass


def multiplication():
    pass


def division():
    pass
