from unittest import TestLoader, TextTestRunner, TestSuite

from tests.GoogleResultsGetterTest import GoogleResultsGetterTests
from tests.NegativeSentenceCreateorTest import NegativeSentenceCreatorTests
from tests.VerbsFinderTest import VerbsFinderTests

loader = TestLoader()
suite = TestSuite((
    loader.loadTestsFromTestCase(GoogleResultsGetterTests),
    loader.loadTestsFromTestCase(VerbsFinderTests),
    loader.loadTestsFromTestCase(NegativeSentenceCreatorTests)
))

runner = TextTestRunner(verbosity=2)
runner.run(suite)
