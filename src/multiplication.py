def multiplication(tuple):
    """multiplication

    Args:
        tuple (tuple)

    Returns:
        float: result of multiplication between tuples first and second element
    """
    try:
        result = float(tuple[0] * tuple[1])
        return result
    except TypeError as err:
        print(
            f'[MULTIPLICATION] Impossible multiplicate this values: [{err}]')
    except Exception as err:
        print(f'[MULTIPLICATION] Something is wrong: [{err}]')
