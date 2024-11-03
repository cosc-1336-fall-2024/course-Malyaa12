def get_lowest_list_value(numbers):
    if not numbers:
        return None  # Handle the case of an empty list
    
    lowest = numbers[0]  # Assume the first number is the lowest
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

def get_highest_list_value(numbers):
    if not numbers:
        return None  # Handle the case of an empty list

    highest = numbers[0]  # Assume the first number is the highest
    for number in numbers:
        if number > highest:
            highest = number
    return highest
