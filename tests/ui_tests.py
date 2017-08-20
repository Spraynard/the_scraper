import unittest

import os
import sys

sys.path.append('../' + os.path.dirname(__file__) + '/classes')
from UI import UI

# sys.path.append('../' + os.path.dirname(__file__))
# from web_scraper import Web_Scraper

class UITesting(unittest.TestCase):
	
	def setUp(self):

		self.UI = UI()

	def test_small_formatted(self):

		result1 = '#  this  #'
		result2 = '#  is    #'
		result3 = '#  a     #'
		result4 = '#  test  #'

		self.UI.feedIn(['this', 'is', 'a', 'test'])

		self.assertEqual(self.UI.spitOutFormattedLine(), result1)
		self.assertEqual(self.UI.spitOutFormattedLine(), result2)
		self.assertEqual(self.UI.spitOutFormattedLine(), result3)
		self.assertEqual(self.UI.spitOutFormattedLine(), result4)

	def test_small_unformatted(self):

		self.UI.feedIn(['this', 'is', 'a', 'test'])

		self.assertEqual(self.UI.spitOutUnformattedLine(), "this")
		self.assertEqual(self.UI.spitOutUnformattedLine(), "is")
		self.assertEqual(self.UI.spitOutUnformattedLine(), "a")
		self.assertEqual(self.UI.spitOutUnformattedLine(), "test")

	def test_StackSizeError(self):
		stack_size = self.UI._getStackSize()
		assert stack_size == 0

		self.assertRaises(Exception, self.UI.spitOutFormattedLine)

if __name__ == "__main__":
	unittest.main()