from src.get_values import get_values
from src.addition import addition
from src.subtraction import subtraction
from src.multiplication import multiplication
from src.division import division


def main() -> str:
    """main
    """
    try:
        values: tuple = get_values()
        add: float = addition(values)
        sub: float = subtraction(values)
        mul: float = multiplication(values)
        div: float = division(values)

        text_response = f'Addition between {values[0]} and {values[1]} = {add}\nSubtraction between {values[0]} and {values[1]} = {sub}\nMultiplication between {values[0]} and {values[1]} = {mul}\nDivision between {values[0]} and {values[1]} = {div}'
        print(text_response)

        return text_response

    except Exception:
        return None
