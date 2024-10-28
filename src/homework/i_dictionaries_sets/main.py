

from src.homework.i_dictionaries_and_sets.dictionary import get_p_distance_matrix

def main():
    while True:
        print("1 - Get p distance matrix")
        print("2 - Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            dna_lists = []
            print("Enter DNA strings (one per line, type 'done' to finish):")
            while True:
                dna_input = input()
                if dna_input.lower() == 'done':
                    break
                dna_lists.append(list(dna_input.strip()))  # Convert string to list of characters
            
            distance_matrix = get_p_distance_matrix(dna_lists)
            for row in distance_matrix:
                print(" ".join(f"{dist:.5f}" for dist in row))
        
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
