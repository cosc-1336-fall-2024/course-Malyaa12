from decisions import get_options_ratio, get_faculty_rating

def main():
    try:
        options = float(input("Enter the number of options: "))
        total = float(input("Enter the total number of items: "))
        
        if total <= 0:
            raise ValueError("Total must be greater than 0")
        
        ratio = get_options_ratio(options, total)
        rating = get_faculty_rating(ratio)
        
        print(f"The faculty rating is: {rating}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
