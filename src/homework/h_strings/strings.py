# src/homework/h_strings/strings.py

def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

def get_dna_complement(dna):
    complement = ""
    for nucleotide in dna:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
        else:
            raise ValueError("Invalid DNA nucleotide")
    return complement[::-1] 


from src.homework.h_strings.value_return import get_hamming_distance
from src.homework.h_strings.value_return import get_dna_complement

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
            complement = get_dna_complement(dna)
            print(f"DNA Complement: {complement}")

        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

    def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Strings must be of the same length")
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

def get_dna_complement(dna):
    complement = ""
    for base in dna:
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
    return complement[::-1]  # Reverse the complement string


