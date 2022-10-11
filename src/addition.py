def addition(tuple):
    """addition

    Args:
        first_value (float): the first float returned from the function get_values()
        second_value (float): the second float returned from the function get_values()

    Returns:
        float: a tuple with the addition of the values received by get_values()
    """
    try:
        result = tuple[0] + tuple[1]
        return result
    except Exception as err:
        print(f'[ADDITION] Something is wrong: [{err}]')
