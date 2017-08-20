# Unit testing file for my web scraper
import unittest

from web_scraper import Web_Scraper

class TestWebScraper(unittest.TestCase):

	def test_init(self):
		website = 'http://localhost:8000'
		scr = Web_Scraper(website)
		self.assertEqual(scr.getWebsite(), 'http://localhost:8000')

if __name__ == '__main__':
	unittest.main()