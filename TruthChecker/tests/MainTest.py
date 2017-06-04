from unittest import TestLoader, TextTestRunner, TestSuite

from TruthChecker.VerbsFinder import VerbsFinder

verbs_finders = VerbsFinder()


def get_verbs_finder():
    return verbs_finders


def run_tests():
    loader = TestLoader()
    from TruthChecker.tests.GoogleResultsGetterTest import GoogleResultsGetterTests
    from TruthChecker.tests.VerbsFinderTest import VerbsFinderTests
    from TruthChecker.tests.NegativeSentenceCreatorTest import NegativeSentenceCreatorTests
    suite = TestSuite((
        loader.loadTestsFromTestCase(GoogleResultsGetterTests),
        loader.loadTestsFromTestCase(VerbsFinderTests),
        loader.loadTestsFromTestCase(NegativeSentenceCreatorTests)
    ))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


run_tests()
