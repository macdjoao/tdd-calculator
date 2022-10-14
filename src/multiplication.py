def multiplication(tuple) -> float:
    """multiplication

    Args:
        tuple (tuple)

    Returns:
        float: result of multiplication between tuples first and second element
    """
    try:
        result: float = float(tuple[0] * tuple[1])
        return result
    except Exception:
        return None
