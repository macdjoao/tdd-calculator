def division(tuple):
    """division

    Args:
        tuple (tuple)

    Returns:
        float: result of division between tuples first and second element
    """
    try:
        result = float(tuple[0] / tuple[1])
        return result
    except ZeroDivisionError as err:
        print(
            f'[DIVISION] It is not possible to divide a number by zero: [{err}]')
    except Exception as err:
        print(f'[DIVISION] Something is wrong: [{err}]')
