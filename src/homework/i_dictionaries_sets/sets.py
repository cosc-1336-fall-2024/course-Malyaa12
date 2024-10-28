import unittest
from src.homework.i_dictionaries_and_sets.dictionary import get_p_distance, get_p_distance_matrix

class TestConfig(unittest.TestCase):

    def test_p_distance(self):
        result = get_p_distance(['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
                                 ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'])
        self.assertAlmostEqual(result, 0.4, places=3)

    def test_get_p_distance_matrix(self):
        dna_lists = [
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
            ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],
            ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        ]
        expected_matrix = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        result = get_p_distance_matrix(dna_lists)
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                self.assertAlmostEqual(result[i][j], expected_matrix[i][j], places=3)

if __name__ == "__main__":
    unittest.main()
