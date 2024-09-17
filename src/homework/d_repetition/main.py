# src/homework/d_repetition/main.py

from repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Select an option (1, 2, 3): ")

        if choice == '1':
            num = int(input("Enter a number (0 < num < 10): "))
            while num <= 0 or num >= 10:
                print("Invalid input. Please enter a number greater than 0 and less than 10.")
                num = int(input("Enter a number (0 < num < 10): "))
            result = get_factorial(num)
            print(f"The factorial of {num} is {result}.")

        elif choice == '2':
            num = int(input("Enter a number (0 < num < 100): "))
            while num <= 0 or num >= 100:
                print("Invalid input. Please enter a number greater than 0 and less than 100.")
                num = int(input("Enter a number (0 < num < 100): "))
            result = sum_odd_numbers(num)
            print(f"The sum of odd numbers up to {num} is {result}.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")

        exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
        if exit_choice == 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
