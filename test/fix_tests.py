#!/usr/bin/env python

import unittest
from src.fix import contains_3_or_more_numbers_in_a_row,\
        remove_protein_homolog, remove_fragment,\
        remove_kDa, fix_anno

class TestFix(unittest.TestCase):

    def setUp(self):
        pass

    def test_fix_anno_no_change(self):
        annos = ["Zinc finger protein 800",
                "Uncharacterized protein LOC285141",
                "Transmembrane and TPR repeat-containing protein CG4341",
                "putative WD repeat-containing protein alr3466",
                "Protein FAM116B",
                "Protein crumbs",
                "Zygotic gap protein knirps"]
        for anno in annos:
            self.assertEqual(anno, fix_anno(anno))

    def test_fix_anno_single_error(self):
        annos = ["O-acetyl-ADP-ribose deacetylase C6orf130 homolog",
                "Kinase D-interacting substrate of 220 kDa",
                "putative E3 ubiquitin-protein ligase DDB_G0283893",
                "UPF0202 protein (Fragment)"]

        expected = ["O-acetyl-ADP-ribose deacetylase C6orf130",
            "Kinase D-interacting substrate",
            "putative E3 ubiquitin-protein ligase DDB_G0283893",
            "UPF0202 protein"]
        for i, anno in enumerate(annos):
            self.assertEqual(expected[i], fix_anno(anno))

    def test_fix_anno_multiple_errors(self):
        annos = ["300 kDa antigen AG231 (Fragment)",
                "Transmembrane protein C6orf70 homolog (Fragment)"]
        expected = ["antigen AG231", "Transmembrane protein C6orf70"]
        for i, anno in enumerate(annos):
            self.assertEqual(expected[i], fix_anno(anno))

    def test_fix_anno_from_dict(self):
        annos = ["EMILIN-2", 
                "Staphylococcal nuclease domain-containing protein 1"]
        expected = ["Elastin microfibril interface-located protein 2",
                "Nuclease domain-containing protein 1"]
        for i, anno in enumerate(annos):
            self.assertEqual(expected[i], fix_anno(anno))

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

    def test_remove_fragment(self):
        annos = ["kDa antigen (Fragment)", "Collagen alpha-2(I) chain (Fragments)", "Protein crumbs"]
        expected = ["kDa antigen", "Collagen alpha-2(I) chain", "Protein crumbs"]
        for i, anno in enumerate(annos):
            self.assertEqual(expected[i], remove_fragment(anno))

    def test_remove_kDa(self):
        annos = ["12 kDa FK506-binding protein", 
                "Centriolar coiled-coil protein of 110 kDa", "Protein crumbs"]
        expected = ["FK506-binding protein", "Centriolar coiled-coil protein", 
                "Protein crumbs"]
        for i, anno in enumerate(annos):
            self.assertEqual(expected[i], remove_kDa(anno))

##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFix))
    return suite

if __name__ == '__main__':
    unittest.main()
