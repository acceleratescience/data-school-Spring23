import unittest
import dna

class TestDNACount(unittest.TestCase):

    def test_A_nucleotide(self):
        test_input = 'A'
        expected_output = (1,0,0,0)
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_C_nucleotide(self):
        test_input = 'C'
        expected_output = (0,1,0,0)
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_G_nucleotide(self):
        test_input = 'G'
        expected_output = (0,0,1,0)
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_T_nucleotide(self):
        test_input = 'T'
        expected_output = (0,0,0,1)
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_empty_sequence(self):
        test_input = ''
        expected_output = (0,0,0,0)
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_garbage_sequence(self):
        test_input = 'AXXGT'
        expected_output = "Input DNA sequence is not valid."
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_complicated_sequence(self):
        test_input = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        expected_output = (20,12,17,21)
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_constraint_length(self):
        test_input = 'A'*1001
        assert(len(test_input) > 1000)
        expected_output = "Input DNA sequence length is above allowed limit."
        actual_output = dna.get_dna_count_first_attempt(test_input)
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
