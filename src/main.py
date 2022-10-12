from src.get_values import get_values
from src.addition import addition
from src.subtraction import subtraction
from src.multiplication import multiplication
from src.division import division


def main():
    """main
    """
    try:
        values = get_values()
        add = addition(values)
        sub = subtraction(values)
        mul = multiplication(values)
        div = division(values)

        print(f'Addition between {values[0]} and {values[1]} = {add}')
        print(f'Subtraction between {values[0]} and {values[1]} = {sub}')
        print(f'Multiplication between {values[0]} and {values[1]} = {mul}')
        print(f'Division between {values[0]} and {values[1]} = {div}')

    except Exception as err:
        print(f'[MAIN] Something is wrong: [{err}]')
