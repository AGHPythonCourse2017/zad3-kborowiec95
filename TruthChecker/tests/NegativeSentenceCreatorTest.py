import unittest

from TruthChecker.NegativeSentenceCreator import *


class NegativeSentenceCreatorTests(unittest.TestCase):
    from TruthChecker.VerbsFinder import VerbsFinder
    vf = VerbsFinder()

    def test_get_negative_verb(self):
        self.assertEquals(("did not create", 1), get_negative_verb("I created car", self.vf)[0:2])
        self.assertEquals(("did not move", 1), get_negative_verb("He moved the", self.vf)[0:2])
        self.assertEquals(("did not test", 2), get_negative_verb("I only tested the", self.vf)[0:2])

        self.assertEquals(("do not create", 1), get_negative_verb("I create car", self.vf)[0:2])
        self.assertEquals(("does not create", 1), get_negative_verb("He creates car", self.vf)[0:2])
        self.assertEquals(("does not move", 1), get_negative_verb("She moves car", self.vf)[0:2])
        self.assertEquals(("does not test", 2), get_negative_verb("It only tests car", self.vf)[0:2])

    def test_get_negative_sentence(self):
        self.assertEquals("fsdfsds ggffdg", get_negative_sentence("fsdfsds not ggffdg", self.vf))
        self.assertEquals("He does not cook dinner", get_negative_sentence("He cooks dinner", self.vf))
        self.assertEquals("He is not cooking", get_negative_sentence("He is cooking", self.vf))
        self.assertEquals("He did not cook", get_negative_sentence("He cooked", self.vf))
        self.assertEquals("He was not cooking", get_negative_sentence("He was cooking", self.vf))
        self.assertEquals("He has not been cooking", get_negative_sentence("He has been cooking", self.vf))
        self.assertEquals("He had not cooked", get_negative_sentence("He had cooked", self.vf))
        self.assertEquals("He had not been cooking", get_negative_sentence("He had been cooking", self.vf))
        self.assertEquals("He will not cook", get_negative_sentence("He will cook", self.vf))
        self.assertEquals("He will not be cooking", get_negative_sentence("He will be cooking", self.vf))
        self.assertEquals("He would not be cooking", get_negative_sentence("He would be cooking", self.vf))
        self.assertEquals("He could not cook", get_negative_sentence("He could cook", self.vf))
