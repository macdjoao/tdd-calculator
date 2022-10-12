def multiplication(tuple):
    """multiplication

    Args:
        tuple (tuple)

    Returns:
        float: result of multiplication between tuples first and second element
    """
    try:
        result = tuple[0] * tuple[1]
        return result
    except Exception as err:
        print(f'[MULTIPLICATION] Something is wrong: [{err}]')
