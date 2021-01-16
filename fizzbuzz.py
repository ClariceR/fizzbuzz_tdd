

def is_divisible_by(number, divisor):
    return number % divisor == 0


def say(number):
    if is_divisible_by(number, 3) and is_divisible_by(number, 5):
        return 'fizzbuzz'
    elif is_divisible_by(number, 3):
        return 'fizz'
    elif is_divisible_by(number, 5):
        return 'buzz'
    else:
        return number


