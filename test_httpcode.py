import unittest
import json
import os
from httpcode import search_code, load_codes

class TestHttpCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.codes = load_codes()

    def test_json_validity(self):
        """Verify that codes.json is a valid JSON and not empty."""
        self.assertTrue(len(self.codes) > 0)
        for item in self.codes:
            self.assertIn('code', item)
            self.assertIn('phrase', item)
            self.assertIn('class', item)

    def test_search_by_code(self):
        """Verify searching by specific HTTP code."""
        results = search_code("404", self.codes)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['phrase'], "Not Found")

    def test_search_by_keyword(self):
        """Verify searching by keyword in phrase or description."""
        results = search_code("timeout", self.codes)
        self.assertTrue(len(results) > 0)
        # Check if all results contain 'timeout'
        for res in results:
            match = "timeout" in res['phrase'].lower() or "timeout" in res['description'].lower()
            self.assertTrue(match)

    def test_filter_by_class(self):
        """Verify filtering by class (e.g., 2xx, 4xx)."""
        results = search_code("2xx", self.codes)
        self.assertTrue(len(results) > 0)
        for res in results:
            self.assertTrue(res['class'].startswith("2xx"))

    def test_search_no_results(self):
        """Verify search returns empty list for non-existent query."""
        results = search_code("nonexistentquery123", self.codes)
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()
