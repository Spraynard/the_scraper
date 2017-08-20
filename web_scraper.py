import sys
import os

import requests
import lxml

from bs4 import BeautifulSoup
from mechanize import Browser

sys.path.append(os.path.dirname(__file__) + '/classes')
from UI import UI

class Web_Scraper:

	def __init__(self, website):
		# Website the scraper will be on 
		self.website = website
		# Browser initialization
		self.browser = Browser()
		# Will contain responses from browser
		self.response = None
		self.request = None
		self.response = None
		self.links = None

	def showSelfLinks(self):
		return self.links

	def getWebsite(self):
		return self.website
		
	def get(self):
		self.response = self.browser.open(self.website)

	def goBack(self):
		self.response = self.browser.back()

	def printTitle(self):
		print self.browser.title()

	def printForms(self):
		for form in self.browser.forms():
			print "Form Name:", form.name
			print form

	def selectForm(self, name, number = None):
		if (number):
			self.browser = list(self.getForms())[number]
		else:
			self.browser.select_form(name)

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

	def getLinks(self):
		user_value = None
		self.links = {}
		links = self.browser.links()
		for link in links:
			self.links[links.index(link)] = {"link" : link}
			print "#" + str(links.index(link)), link.text, link.url
		while not raw_input("Do you want to follow any links(Y/N): ").upper() == "N":
			user_value = raw_input("Which link would you like to follow (input link #): ")
			if not int(user_value) in self.links.keys():
				print "That is not a valid link number"
				continue
			else:
				didFollowLink = self.followLink(int(user_value))
				if not didFollowLink:
					print "There was a problem with following that link. Please try again"
				else:
					print "Link Followed"
					break

	def followLink(self, linkNumber):
		try:
			self.response = self.browser.follow_link(self.links[linkNumber]["link"])
			return True
		except:
			return False

	def printResponse(self):
		print self.response.read()

	def parseResponse(self):
		return BeautifulSoup(self.response, 'lxml').prettify()
