import unittest

from src.examples.h_strings.strings import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

# tests/homework/h_strings/test_strings.py

import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        result = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        self.assertEqual(result, 7)

    def test_get_dna_complement(self):
        result = get_dna_complement("AAAACCCGGT")
        self.assertEqual(result, "ACCGGGTTTT")

if __name__ == '__main__':
    unittest.main()
