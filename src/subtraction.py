def subtraction(tuple):
    """subtraction

    Args:
        tuple (tuple)

    Returns:
        float: result of subtraction between tuples first and second element
    """
    try:
        result = tuple[0] - tuple[1]
        return result
    except Exception as err:
        print(f'[SUBTRACTION] Something is wrong: [{err}]')
