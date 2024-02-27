def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]
    
def calculate_mode(numbers):
    mode = max(set(numbers), key = numbers.count)
    return mode