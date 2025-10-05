import random

DESCRIPTION = "What number is missing in the progression?"


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = random.randint(5, 10)

    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(str(x) for x in progression)

    return question, correct_answer