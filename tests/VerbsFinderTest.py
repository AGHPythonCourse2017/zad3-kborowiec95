import unittest
from src.VerbsFinder import *


class VerbsFinderTests(unittest.TestCase):
    vf = VerbsFinder()

    def test_parse_html(self):
        self.assertEquals(1000, len(self.vf.verbs_list_base))
        self.assertEquals(1000, len(self.vf.verbs_list_past_simple))
        self.assertEquals(1000, len(self.vf.verbs_list_pres_simple))

    def test_binary_search(self):
        self.assertEquals(2, self.vf.binary_search([1, 2, 3, 4, 5], 3))
        self.assertEquals(-1, self.vf.binary_search([], 0))
        self.assertEquals(0, self.vf.binary_search([1, 2, 3, 4, 5], 1))
        self.assertNotEqual(4, self.vf.binary_search([1, 2, 3, 5, 4], 4))
        self.assertEquals(4, self.vf.binary_search([1, 2, 3, 4, 5], 5))

    def test_is_base_verb(self):
        self.assertTrue(self.vf.is_base_verb("create"))
        self.assertFalse(self.vf.is_base_verb(" create"))
        self.assertTrue(self.vf.is_base_verb("test"))
        self.assertFalse(self.vf.is_base_verb(" test "))
        self.assertFalse(self.vf.is_base_verb(" fds sdfsd"))

    def test_is_pres_simple_verb(self):
        self.assertTrue(self.vf.is_pres_simple_verb("creates"))
        self.assertFalse(self.vf.is_pres_simple_verb(" creates  "))
        self.assertTrue(self.vf.is_pres_simple_verb("tests"))
        self.assertFalse(self.vf.is_pres_simple_verb(" tests "))
        self.assertFalse(self.vf.is_pres_simple_verb(" fds sdfsd"))

    def test_is_past_simple_verb(self):
        self.assertTrue(self.vf.is_past_simple_verb("created"))
        self.assertFalse(self.vf.is_past_simple_verb(" created  "))
        self.assertTrue(self.vf.is_past_simple_verb("tested"))
        self.assertFalse(self.vf.is_past_simple_verb(" tested "))
        self.assertFalse(self.vf.is_past_simple_verb(" fds sdfsd"))

    def test_find_verb(self):
        self.assertEqual(("are", 4), self.vf.find_verb("Test created by me are good"))
        self.assertEqual(("created", 1), self.vf.find_verb("Test created here"))
        self.assertEqual(("water", 1), self.vf.find_verb("The water boils in 100 degrees"))
        self.assertEqual(("boils", 2), self.vf.find_verb("Almost everything boils in 10000000 degrees"))
        self.assertEqual(("are", 3), self.vf.find_verb("The greatest codetricks are here"))
        self.assertEqual("",self.vf.find_verb("fsffsdfsfsd"))
        self.assertEqual("", self.vf.find_verb("fsffsdfsfs  sfsdf  fd fs fdsf  dfsd"))
        self.assertEqual("", self.vf.find_verb(""))

