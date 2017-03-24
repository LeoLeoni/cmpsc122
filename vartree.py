class VarTree:
	"""A binary search tree that stores a variable and its value"""

	class Node:
		__slots__ = "_left", "_right", "_var", "_value"
		def __init__(self, l, variable, val, r):
			self._left = l
			self._right = r
			self._var = variable
			self._value = val
			
	__slots__ = "_root", "_size"

	def __init__ (self):
		"""Initializes an empty tree"""
		self._root = None
		self._size = 0

	def _search(self, here, var):
		if here is None:
			return 0
		elif var == here._var:
			return here			#i guess it should return the whole node?
		elif var < here._var:
			return self._search(here._left, var)
		elif var > here._var:
			return self._search(here._right, var)
	
	def _insert(self, here, var, value):
		if here is None:
			self._size += 1
			return self.Node(None, var, value, None)		#the new leaf
		elif here < here._var:
			return self.Node(   self._insert(here._left, var, value),   here._var, here._value, here._right)
		elif here > here._var:
			return self.Node(here._left, here._var, here._value,    self._insert(here._right, var, value)    )
		elif here == here._var:
			return self.Node(here._left, here._var, value, here._right)		#reassignment - changes only the value

	def assign(self, var, value):
		"""Assigns a value to a variable whether it previously existed or not"""
		self._root = self._insert(self._root, var, value)
	
	def lookup(self, var):
		"""Finds the value of the variable. Defaults to 0"""
		searched = self._search(self._root, var)
		if searched is not None:
			return searched._value
		else:
			self._assign(var, 0)	#creates the new variable to 0
			return 0
	
	def is_empty(self):
		return (self._size == 0)

	def __len__ (self):
		return self._size