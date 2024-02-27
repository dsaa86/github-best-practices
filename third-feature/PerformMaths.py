from FirstNewFeature.FirstNewFeature import (addTwoNumbers, cubeRoot,
                                             divideTwoNumbers,
                                             multiplyTwoNumbers, powerOfTwo,
                                             squareRoot, subtractTwoNumbers)
from FirstNewFeature.MoreMaths import calculate_mean


def performCoolMathsTrick(param_one: int, param_two: int, param_three: int, param_four: int, param_five: int, param_six: int, param_seven: int):
    first_number = addTwoNumbers(param_one, param_two)
    second_number = multiplyTwoNumbers(param_three, param_four)
    third_number = subtractTwoNumbers(param_five, param_six)
    fourth_number = divideTwoNumbers(param_seven, param_four)
    fifth_number = powerOfTwo(param_five)
    sixth_number = squareRoot(param_six)
    seventh_number = cubeRoot(param_seven)

    numbers = [first_number, second_number, third_number, fourth_number, fifth_number, sixth_number, seventh_number]

    return calculate_mean(numbers)
