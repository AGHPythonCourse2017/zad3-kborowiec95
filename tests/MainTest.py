from unittest import TestLoader, TextTestRunner, TestSuite

from tests.GoogleResultsGetterTest import GoogleResultsGetterTests
from tests.NegativeSentenceCreatorTest import NegativeSentenceCreatorTests
from tests.VerbsFinderTest import VerbsFinderTests
from src.VerbsFinder import VerbsFinder

verbs_finders = VerbsFinder()


def get_verbs_finder():
    return verbs_finders


loader = TestLoader()
suite = TestSuite((
    loader.loadTestsFromTestCase(GoogleResultsGetterTests),
    loader.loadTestsFromTestCase(VerbsFinderTests),
    loader.loadTestsFromTestCase(NegativeSentenceCreatorTests)
))

runner = TextTestRunner(verbosity=2)
runner.run(suite)
