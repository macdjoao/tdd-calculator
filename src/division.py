def division(tuple) -> float:
    """division

    Args:
        tuple (tuple)

    Returns:
        float: result of division between tuples first and second element
    """
    try:
        result: float = float(tuple[0] / tuple[1])
        return result
    except ZeroDivisionError:
        return (f'It is not possible to divide a number by zero')
    except Exception:
        return None
