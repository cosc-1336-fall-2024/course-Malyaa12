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
    return complement[::-1]  # Reverse the string to get the reverse complement
