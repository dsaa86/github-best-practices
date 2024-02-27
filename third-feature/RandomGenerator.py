from random import randint


def generateRandomNumber(lower_bound: int = 0, upper_bound: int = 100):
    return randint(lower_bound, upper_bound)