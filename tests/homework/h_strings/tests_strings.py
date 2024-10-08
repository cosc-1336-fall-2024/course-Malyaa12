import unittest
from src.homework.h_strings.value_return import get_hamming_distance
from src.homework.h_strings.value_return import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        # Test with the provided example
        result = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        self.assertEqual(result, 7)

    def test_get_dna_complement(self):
        # Test with the provided example
        result = get_dna_complement("AAAACCCGGT")
        self.assertEqual(result, "ACCGGGTTTT")

    def test_empty_strings(self):
        # Test Hamming distance with empty strings
        result = get_hamming_distance("", "")
        self.assertEqual(result, 0)

    def test_no_difference(self):
        # Test Hamming distance with identical strings
        result = get_hamming_distance("AAAA", "AAAA")
        self.assertEqual(result, 0)

    def test_all_differences(self):
        # Test Hamming distance with completely different strings
        result = get_hamming_distance("ATCG", "TAGC")
        self.assertEqual(result, 4)

    def test_single_base_complement(self):
        # Test complement for single bases
        self.assertEqual(get_dna_complement("A"), "T")
        self.assertEqual(get_dna_complement("T"), "A")
        self.assertEqual(get_dna_complement("C"), "G")
        self.assertEqual(get_dna_complement("G"), "C")

    def test_longer_string_complement(self):
        # Test with longer DNA strings
        result = get_dna_complement("GTCA")
        self.assertEqual(result, "TGAC")

    def test_invalid_hamming_distance(self):
        # Test for ValueError with strings of different lengths
        with self.assertRaises(ValueError):
            get_hamming_distance("AAG", "AA")

if __name__ == "__main__":
    unittest.main()




    import unittest
from src.homework.h_strings.value_return import get_hamming_distance
from src.homework.h_strings.value_return import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        result = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        self.assertEqual(result, 7)

    def test_get_dna_complement(self):
        result = get_dna_complement("AAAACCCGGT")
        self.assertEqual(result, "ACCGGGTTTT")
        
    def test_empty_string(self):
        result = get_hamming_distance("", "")
        self.assertEqual(result, 0)

    def test_no_difference(self):
        result = get_hamming_distance("AAAA", "AAAA")
        self.assertEqual(result, 0)

    def test_all_differences(self):
        result = get_hamming_distance("ATCG", "TAGC")
        self.assertEqual(result, 4)

    def test_single_base_complement(self):
        self.assertEqual(get_dna_complement("A"), "T")
        self.assertEqual(get_dna_complement("T"), "A")
        self.assertEqual(get_dna_complement("C"), "G")
        self.assertEqual(get_dna_complement("G"), "C")

if __name__ == "__main__":
    unittest.main()


