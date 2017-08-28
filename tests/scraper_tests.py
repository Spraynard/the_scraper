# Unit testing file for my web scraper
import unittest

import os
import sys

sys.path.append('../classes')
from web_scraper import Web_Scraper

class TestWebScraper(unittest.TestCase):

	def test_init(self):
		website = 'http://localhost:8000'
		scr = Web_Scraper(website)
		self.assertEqual(scr.getWebsite(), 'http://localhost:8000')

	def test_scraper(self):
		website = 'http://localhost:8000'
		scr = Web_Scraper(website)
		scr.get()
		print scr.scrapeAllData('a')

if __name__ == '__main__':
	unittest.main()