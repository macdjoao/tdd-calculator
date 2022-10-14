def subtraction(tuple) -> float:
    """subtraction

    Args:
        tuple (tuple)

    Returns:
        float: result of subtraction between tuples first and second element
    """
    try:
        result: float = float(tuple[0] - tuple[1])
        return result
    except Exception:
        return None
