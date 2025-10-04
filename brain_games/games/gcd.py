import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."

def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer