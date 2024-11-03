from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

def main():
    numbers = []
    
    while True:
        print("Menu:")
        print("1. Show the list low/high values")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            while True:
                value = input("Enter a list value (or type 'done' to finish): ")
                if value.lower() == 'done':
                    break
                try:
                    number = float(value)  # Convert input to float
                    numbers.append(number)
                except ValueError:
                    print("Please enter a valid number.")

            if len(numbers) >= 3:
                print(f"The lowest number is: {get_lowest_list_value(numbers)}")
                print(f"The highest number is: {get_highest_list_value(numbers)}")
            else:
                print("Please enter at least 3 values before checking low/high values.")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
