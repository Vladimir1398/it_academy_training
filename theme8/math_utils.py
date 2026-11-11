def square(number):
    return number * number

def cube(number):
    return number * number * number


def is_even(number):
    return number % 2 == 0


def factorial(number):
    if not isinstance(number, int):
        return None
    if number < 0:
        return None
    result = 1
    
    for i in range(2, number + 1):
        result *= i
    return result
 
 
def max_of_two(a, b):
    return a if a > b else b