

def get_factorial(num):
    """Calculate the factorial of a given number."""
    if num < 0:
        return None  # Factorial is not defined for negative numbers
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
def sum_odd_numbers(num):
    """Calculate the sum of odd numbers up to the given number."""
    if num < 0:
        return None  # Sum is not defined for negative numbers
    total = 0
    for i in range(1, num + 1, 2):  # Iterate only odd numbers
        total += i
    return total
