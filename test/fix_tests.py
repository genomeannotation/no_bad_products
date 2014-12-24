#!/usr/bin/env python

import unittest
from src.fix import contains_3_or_more_numbers_in_a_row,\
        remove_protein_homolog, fix_plural, remove_fragment

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

    def test_remove_protein_homolog1(self):
        anno = "Transmembrane protein C6orf70 homolog (Fragment)"
        expected = "Transmembrane protein C6orf70 (Fragment)"
        actual = remove_protein_homolog(anno)
        self.assertEqual(expected, actual)

    def test_remove_protein_homolog2(self):
        anno = "DnaJ protein homolog 1"
        expected = "DnaJ 1"
        actual = remove_protein_homolog(anno)
        self.assertEqual(expected, actual)

    def test_remove_protein_homolog3(self):
        anno = "Neurogenic locus notch homolog protein 3"
        expected = "Neurogenic locus notch 3"
        actual = remove_protein_homolog(anno)
        self.assertEqual(expected, actual)

    def test_fix_plural_no_change(self):
        no_change = ["Protein crumbs", "PHD finger protein rhinoceros"]
        for anno in no_change:
            self.assertEqual(anno, fix_plural(anno))

    def test_remove_fragment(self):
        annos = ["kDa antigen (Fragment)", "Collagen alpha-2(I) chain (Fragments)", "Protein crumbs"]
        expected = ["kDa antigen", "Collagen alpha-2(I) chain", "Protein crumbs"]
        for i, anno in enumerate(annos):
            self.assertEqual(expected[i], remove_fragment(anno))


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFix))
    return suite

if __name__ == '__main__':
    unittest.main()
