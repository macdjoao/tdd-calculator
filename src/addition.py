def addition(tuple) -> float:
    """addition

    Args:
        tuple (tuple)

    Returns:
        float: result of addition between tuples first and second element
    """
    try:
        result: float = float(tuple[0] + tuple[1])
        return result
    except Exception:
        return None
