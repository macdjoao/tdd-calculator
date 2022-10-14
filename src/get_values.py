def get_values() -> float:
    """get_values

    Returns:
        float: a tuple with the user inputs
    """
    try:
        first_value: float = float(input('Type the first number: '))
        second_value: float = float(input('Type the second number: '))
        return (first_value, second_value)
    except (NameError, ValueError):
        print(
            f'[GET_VALUES] You must give a two numbers (int or float) for the function')
    except Exception:
        return None
