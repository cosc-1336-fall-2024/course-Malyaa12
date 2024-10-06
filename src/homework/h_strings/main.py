# src/homework/h_strings/main.py

from strings import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("Menu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")
            try:
                distance = get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance: {distance}")
            except ValueError as e:
                print(e)
        
        elif choice == '2':
            dna = input("Enter DNA string: ")
            try:
                complement = get_dna_complement(dna)
                print(f"DNA Complement: {complement}")
            except ValueError as e:
                print(e)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
