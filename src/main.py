from src.get_values import get_values
from src.addition import addition
from src.subtraction import subtraction
from src.multiplication import multiplication
from src.division import division


def main():
    try:
        values = get_values()
        add = addition(values)
        sub = subtraction(values)
        mul = multiplication(values)
        div = division(values)

        print(f'Addition between {values} = {add}')
        print(f'Subtraction between {values} = {sub}')
        print(f'Multiplication between {values} = {mul}')
        print(f'Division between {values} = {div}')

        return values, add, sub, mul, div

    except Exception as err:
        print(f'[MAIN] Something is wrong: [{err}]')
