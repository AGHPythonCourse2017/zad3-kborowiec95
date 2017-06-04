import unittest

from GoogleResultsGetter import GoogleResultsGetter


class GoogleResultsGetterTests(unittest.TestCase):
    dummy_gsg = GoogleResultsGetter("USER_KEY", "CUSTOM_SEARCH_ID")

    def test_create_google_request(self):
        self.assertEqual("test+test+test", self.dummy_gsg.create_google_request("   test   test    test    "))
        self.assertEqual("", self.dummy_gsg.create_google_request(""))
        self.assertNotIn(" ", self.dummy_gsg.create_google_request("f sf sf dsf s f"))
        self.assertNotIn(" ", self.dummy_gsg.create_google_request("                 "))
        self.assertEqual(self.dummy_gsg.create_google_request("+++++++++++"),
                         self.dummy_gsg.create_google_request("+++++++++++"))

    def test_create_url(self):
        r = self.dummy_gsg.create_google_request("    f sf sf ds  fd   f   df fsd s f")
        self.assertNotIn(" ", self.dummy_gsg.create_url(r))

        r = self.dummy_gsg.create_google_request("f sf sf ds  fd   f   df fsd s f    ")
        self.assertNotIn(" ", self.dummy_gsg.create_url(r))

        r = self.dummy_gsg.create_google_request(" fds fs sd")
        self.assertEqual("https://", self.dummy_gsg.create_url(r)[0:8])

        r = self.dummy_gsg.create_google_request(" test  test")
        self.assertEqual("https://", self.dummy_gsg.create_url(r)[0:8])

        r = self.dummy_gsg.create_google_request(" fds fs sd")
        self.assertTrue("+" in self.dummy_gsg.create_url(r))

        r = self.dummy_gsg.create_google_request("tet test")
        self.assertIn("cx=CUSTOM_SEARCH_ID", self.dummy_gsg.create_url(r))
        self.assertIn("?key=USER_KEY", self.dummy_gsg.create_url(r))

        r = self.dummy_gsg.create_google_request(" test ")
        start = "https://www.googleapis.com/customsearch/v1"
        self.assertEquals(start, self.dummy_gsg.create_url(r)[0:len(start)])
