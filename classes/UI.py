from collections import deque

class UI:

	def __init__(self, debug = False):
		self.debug = debug

		self.input = True #True: program accepting input, False: Outputting

		# Bool telling if there's a positive size difference
		#  between input and currentFeedMax
		self.sizeDiff = False

		# Largest size input string currently
		self.currentFeedMax = None

		# The largest size input string will then be transferred to this variable
		self.h_size = None

		# I/O stack
		self.stack = deque()

		# Is the number of lines in stack
		self.stackSize = 0

	def _setHSize(self, size):
		if self.debug:
			print "Setting h_size from", self.h_size, "to value:", size
		self.h_size = size

	def _getHSize(self):
		return self.h_size

	def _getCurrentFeedMax(self):
		if self.debug:
			print "This is the value of Current Feed Max:", self.currentFeedMax
		return self.currentFeedMax

	def _setCurrentFeedMax(self, value):
		if self.debug:
			print "currentFeedMax Value =", self.currentFeedMax, "Setting to Value=", value
		self.currentFeedMax = value


	def _digest(self):
		# This function will be used to perform operations on input. I'm not sure what though.
		# Currently sets `h_size` to `currentfeedmax`
		if self.debug:
			print "\n"
			print "Digesting"
			print "\n"

		self._setHSize(self._getCurrentFeedMax())
		self._setSizeDiff(False)

	def _isSizeDiff(self):
		if self.debug:
			print "Checking size diff. Currently:", self.sizeDiff
		return self.sizeDiff

	def _setSizeDiff(self, boolean):
		if self.debug:
			print "Setting sizeDiff from:", self.sizeDiff, "to this:", boolean
		if not isinstance(boolean, bool):
			raise ValueError("You are not putting in a boolean to this function")
		else:
			if boolean == self.sizeDiff:
				return
			self.sizeDiff = boolean

	def _stackSizeUp(self):
		self.stackSize += 1

	def _stackSizeDown(self):
		self.stackSize -= 1

	def _getStackSize(self):
		return self.stackSize 

	def _formatted(self, string):
		s = self._getHSize()
		left = '{:3}'.format('#')
		center = '{:<{width}}'.format(string, width = s)
		right = '{:>3}'.format('#')

		if self.debug:
			print "This is the string i'm getting: ", string
			print "This is S:", s

		return left + center + right

	def _isMax(self, string):
		# Checks if the given string has a length greater than max length
		#	returns a Truthy if the case, falsy if not.
		strlen = len(string)

		# DEBUG
		if self.debug:
			print "Method: isMax(), String Length:", strlen

		if not self.currentFeedMax:
			# DEBUG
			if self.debug:
				print "Method: isMax() Current Feed Max being changed from initialization"

			self._setCurrentFeedMax(strlen)
			return True
		elif self._getCurrentFeedMax() < strlen:
			self._setCurrentFeedMax(strlen)
			return True
		return False

	def _prependStack(self, string):
		self.stack.appendleft(string)

	def _popStack(self):
		return self.stack.pop()

	def _feedOperation(self, string):
		self._setSizeDiff(self._isMax(string))
		self._prependStack(string)
		self._stackSizeUp()
		if self._isSizeDiff():
			self._digest()

	def feedIn(self, inputData):
	# Summary: Feeds input into `self.stack`
	# Input: `input` - Self explanatory. Can be either a list or a string.
	# Returns: None - Only applies operations
		if isinstance(inputData, list):
			# If `inputData` is a list
			for string in inputData:
				self._feedOperation(string)

		elif isinstance(inputData, str):
			# If `inputData` is a string
			self._feedOperation(inputData)

	def spitOutFormattedLine(self):
		if self._getStackSize() == 0:
		# Works coherently with the Try/Except block in formatted flush
			raise Exception
		else:
			self._stackSizeDown()
			return self._formatted(self._popStack())

	def spitOutUnformattedLine(self):
		if self._getStackSize() == 0:
			raise Exception
		else:
			self._stackSizeDown()
			return self._popStack()

	def formattedFlush(self):
		while True:
			try:
				print self._spitOutFormattedLine()
			except:
				break

	def unformattedFlush(self):
		while True:
			try:
				print self._spitOutUnformattedLine()
			except:
				break

