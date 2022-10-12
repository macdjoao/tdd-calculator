def addition(tuple):
    """addition

    Args:
        tuple (tuple)

    Returns:
        float: result of addition between tuples first and second element
    """
    try:
        result = float(tuple[0] + tuple[1])
        return result
    except Exception as err:
        print(f'[ADDITION] Something is wrong: [{err}]')
