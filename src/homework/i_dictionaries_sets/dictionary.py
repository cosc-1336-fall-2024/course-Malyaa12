

def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length.")
    
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    return differences / len(list1)

def get_p_distance_matrix(dna_lists):
    n = len(dna_lists)
    p_distance_matrix = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                p_distance_matrix[i][j] = get_p_distance(dna_lists[i], dna_lists[j])
    
    return p_distance_matrix
