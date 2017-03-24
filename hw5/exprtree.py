from abc import ABCMeta, abstractmethod
from vartree import vartree

class ExprTree(metaclass = ABCMeta):
	"""Abstract class for expression"""
	def __str__(self):
		return ' '.join(str(x)for x in iter(self))

	@abstractmethod
	def __iter__(self):
		"""an inorder iterator for this tree node, for display"""
		pass
	@abstractmethod
	def postfix(self):
		"""a post-order iterator to create a postfix expression"""
		pass
	@abstractmethod
	def evaluate(self, variables):
		"""evaluate using the existing variables"""
		pass

class Var(ExprTree):
	"""A variable leaf"""
	def __init__(self, n):
		self._name = n
	def __iter__(self):
		yield self._name
	def postfix(self):
		yield self._name
	def evaluate(self, variables):
		return variables.lookup(self._name)

class Value(ExprTree):
	"""A value leaf"""
	def __init__ (self, v):
		self._value = v
	def __iter__(self):
		yield self._value
	def postfix(self):
		yield self._name
	def evaluate(self, variables):
		return self._value

class Cond(ExprTree):
	"""A test condition with true/false cases"""
	def __init__ (self, c, t, f):
		self._cond = c
		self._true = t
		self._false = f

	def __iter__(self):
		yield from self._cond
		yield '?'
		yield from self._true
		yield ':'
		yield from self._false

	def postfix(self):

	def evaluate(self, variables):


class Oper(ExprTree):
	
	def __init__ (self, l, s, r):
		self._left = l
		self._oper = s
		self._right = r

	def __iter__(self):
		yield '('
		yield from self._left
		yield from self._oper
		yield from self._right
		yield ')'
	
	def postfix(self):

	def evaluate(self, variables):
		"""Evaluates the expression with support for relational operators."""
		if self._oper != '=':
			return eval(self._left + self._oper + self._right)
		else:
			vartree.assign 