def division(tuple):
    """division

    Args:
        tuple (tuple)

    Returns:
        float: result of division between tuples first and second element
    """
    try:
        result = tuple[0] / tuple[1]
        return result
    except Exception as err:
        print(f'[DIVISION] Something is wrong: [{err}]')
