# test_page_fetcher.py
import unittest
from PageFetcher import PageFetcher

class TestPageFetcher(unittest.TestCase):
    def test_fetch_page(self):
        fetcher = PageFetcher()
        result = fetcher.fetch_page(1)
        self.assertTrue(len(result) > 0, "The fetched page content should not be empty")

if __name__ == '__main__':
    unittest.main()