import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])

    match operator:
        case '+':
            correct_answer = number1 + number2
        case '-':
            correct_answer = number1 - number2
        case '*':
            correct_answer = number1 * number2
        case _:
            raise ValueError('Unexpected operator')

    question = f'{number1} {operator} {number2}'
    return question, str(correct_answer)