import sys
import os

import requests
import lxml

from bs4 import BeautifulSoup
from mechanize import Browser

class Web_Scraper:

	def __init__(self, website):
		# Website the scraper will be on 
		self.website = website
		# Browser initialization
		self.browser = Browser()
		# Will contain responses from browser
		self.response = None
		self.soup = None
		self.request = None
		self.response = None
		self.links = None

	def setResponse(self, operation):
		self.response = operation

	def getResponse(self):
		return self.response

	def getWebsite(self):
		return self.website

	def get(self):
		self.setResponse(self.browser.open(self.getWebsite()))

	def goBack(self):
		self.setResponse(self.browser.back())

	def selectForm(self, name, number = None):
		if (number):
			self.browser = list(self.getForms())[number]
		else:
			self.browser.select_form(name=name)

	def fillForm(self, **kwargs):
		# Fills form values with the possibility of multiple values.
		# 	For example {"name" : ["Kenneth Scott", "Julie Andrews"]}
		#	will fill a form that has a input of "name" with the two names
		#	given above
		if kwargs is not None:
			for key, value in kwargs:
				if isinstance(value, list):
					value = (", ").join(value)
					self.browser[key] = value
				else:
					self.browser[key] = value

	def submitForm(self):
		self.setResponse(self.browser.submit())

	def followLink(self, linkNumber):
		self.setResponse(self.browser.follow_link(nr = linkNumber))

	def setSoup(self):
		self.soup = BeautifulSoup(self.getResponse(), 'html.parser')

	def getSoup(self):
		return self.soup

	def scrapeOneData(self, tagName):
		self.setSoup()
		soupResponse = self.getSoup()

		return soupResponse.tagName

	def scrapeAllData(self, tagName):
		self.setSoup()
		soupResponse = self.getSoup()

		return soupResponse.find_all(tagName)

