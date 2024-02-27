from random import choice, randint


def generateRandomNumber(lower_bound: int = 0, upper_bound: int = 100):
    return randint(lower_bound, upper_bound)


def generateRandomString(length: int = 10):
    return ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))