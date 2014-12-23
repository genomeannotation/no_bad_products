#!/usr/bin/env python

import unittest
from src.fix import contains_3_or_more_numbers_in_a_row, remove_protein_homolog

class TestFix(unittest.TestCase):

    def setUp(self):
        pass

    def test_contains_3_or_more_numbers_in_a_row(self):
        yes = ["abc123", "123", "2a2a22aa222aaa"]
        no = ["12a34", "foo", "12_34", "12.34"]
        for y in yes:
            self.assertTrue(contains_3_or_more_numbers_in_a_row(y))
        for n in no:
            self.assertFalse(contains_3_or_more_numbers_in_a_row(n))

    def test_remove_protein_homolog(self):
        anno = "Transmembrane protein C6orf70 homolog (Fragment)"
        expected = "Transmembrane protein C6orf70 (Fragment)"
        actual = remove_protein_homolog(anno)
        self.assertEqual(expected, actual)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFix))
    return suite

if __name__ == '__main__':
    unittest.main()
