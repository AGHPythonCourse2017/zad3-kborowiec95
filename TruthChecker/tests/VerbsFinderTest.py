import unittest

from VerbsFinder import *


class VerbsFinderTests(unittest.TestCase):
    vf = VerbsFinder()

    def test_parse_html(self):
        self.assertEquals(1000, len(self.vf.verbs_list_base))
        self.assertEquals(1000, len(self.vf.verbs_list_past_simple))
        self.assertEquals(1000, len(self.vf.verbs_list_pres_simple))

    def test_find_index(self):
        self.assertEquals(2, self.vf.find_index([1, 2, 3, 4, 5], 3))
        self.assertEquals(-1, self.vf.find_index([], 0))
        self.assertEquals(0, self.vf.find_index([1, 2, 3, 4, 5], 1))
        self.assertEqual(4, self.vf.find_index([1, 2, 3, 5, 4], 4))
        self.assertEquals(-1, self.vf.find_index([1, 2, 3, 4, 5], 0))
        self.assertEquals(-1, self.vf.find_index([1, 2, 3, 4, 5], 6))
        self.assertEquals(0, self.vf.find_index([1, 2, 3, 4], 1))
        self.assertEquals(1, self.vf.find_index([1, 2, 3, 4], 2))
        self.assertEquals(2, self.vf.find_index([1, 2, 3, 4], 3))
        self.assertEquals(3, self.vf.find_index([1, 2, 3, 4], 4))
        lst = [x for x in range(0, 1000)]
        self.assertEquals(-1, self.vf.find_index(lst, -1))
        self.assertEquals(-1, self.vf.find_index(lst, 1000))
        for i in range(0, 1000):
            self.assertEquals(i, self.vf.find_index(lst, i))

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
        self.assertTrue(self.vf.is_past_simple_verb("abated"))
        self.assertFalse(self.vf.is_past_simple_verb(" created  "))
        self.assertTrue(self.vf.is_past_simple_verb("created"))
        self.assertTrue(self.vf.is_past_simple_verb("moved"))
        self.assertFalse(self.vf.is_past_simple_verb(" tested "))
        self.assertFalse(self.vf.is_past_simple_verb(" fds sdfsd"))

    def test_find_verb(self):
        self.assertEqual(("are", 4), self.vf.find_verb("Test created by me are good"))
        self.assertEqual(("created", 1), self.vf.find_verb("Test created here"))
        self.assertEqual(("water", 1), self.vf.find_verb("The water boils in 100 degrees"))
        self.assertEqual(("boils", 2), self.vf.find_verb("Almost everything boils in 10000000 degrees"))
        self.assertEqual(("are", 3), self.vf.find_verb("The greatest codetricks are here"))
        self.assertEqual(("", ""), self.vf.find_verb("fsffsdfsfsd"))
        self.assertEqual(("", ""), self.vf.find_verb("fsffsdfsfs  sfsdf  fd fs fdsf  dfsd"))
        self.assertEqual(("", ""), self.vf.find_verb(""))
