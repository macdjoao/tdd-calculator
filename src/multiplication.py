def multiplication(tuple):
    """multiplication

    Args:
        first_value (float): the first float returned from the function get_values()
        second_value (float): the second float returned from the function get_values()

    Returns:
        float: a tuple with the multiplication of the values received by get_values()
    """
    try:
        result = tuple[0] * tuple[1]
        return result
    except Exception as err:
        print(f'[MULTIPLICATION] Something is wrong: [{err}]')
