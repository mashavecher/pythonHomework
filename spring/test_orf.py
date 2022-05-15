import unittest
import ORF
import data_for_orf_test


class ORFTest(unittest.TestCase):
    def test_find_orf(self):
        file_name = 'Moraxella_genomic.fna'
        RE = ORF.find_orf(file_name)
        TE = data_for_orf_test.orf
        self.assertEqual(TE, RE)


if __name__ == '__main__':
    unittest.main()
