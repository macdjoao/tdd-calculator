def get_values():
    """get_values

    Returns:
        float: a tuple with the user inputs
    """
    try:
        first_value = float(input('Type the first number: '))
        second_value = float(input('Type the second number: '))
        return (first_value, second_value)
    except NameError as err:
        print(
            f'[GET_VALUES] You must give a two numbers (int or float) for the function: [{err}]')
    except ValueError as err:
        print(
            f'[GET_VALUES] You must give a two numbers (int or float) for the function: [{err}]')
    except Exception as err:
        print(f'[GET_VALUES] Something is wrong: [{err}]')
