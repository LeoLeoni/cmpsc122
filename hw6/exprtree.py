#exec(open("exprtree.py").read())
from abc import ABCMeta, abstractmethod
from vartree import VarTree

class ExprTree(metaclass = ABCMeta):
	"""Abstract class for expression"""
	# "variables" is a VarTree class object 
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
	#evaluate gets called everytime we need a value for something
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
		#for a variable, the function evaluate returns that variables value by calling the vartree lookup function
		return variables.lookup(self._name)

class Value(ExprTree):
	"""A value leaf"""
	def __init__ (self, v):
		self._value = v
	def __iter__(self):
		yield self._value
	def postfix(self):
		yield self._value
	def evaluate(self, variables):
		return self._value

class Cond(ExprTree):
	"""A test condition with true/false cases"""
	def __init__ (self, c, t, f):
		#are all relational expressions
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
		pass			#	cant make a postfix fonditional but the program won't work without this empty function

	def evaluate(self, variables):
		#mux where cond is the selector, false = 0 and true = 1													#this is a long return statement but it works
		return self._cond.evaluate(variables) and self._true.evaluate(variables) or not self._cond.evaluate(variables) and self._false.evaluate(variables)


class Oper(ExprTree):
	"""A mathematical or relational expression"""

	def __init__ (self, l, s, r):
		self._left = l
		self._oper = s
		self._right = r

	def __iter__(self):
		yield '('
		yield from self._left
		yield self._oper
		yield from self._right
		yield ')'

	def postfix(self):
			yield from self._left.postfix()
			yield from self._right.postfix()
			yield self._oper

	def evaluate(self, variables):

		"""Evaluates the expression with support for relational operators."""
		if self._oper != '=':
			#eval() will return a bool given a relational oper, and a number given a arithmetic oper
			return eval(  str(self._left.evaluate(variables))  +  self._oper + str(self._right.evaluate(variables))  )		#needed to convert to string because python is weird
		else:
			#in this case left should always be a var name and right should always be the value being assigned to it
			variables.assign(self._left._name, self._right.evaluate(variables))
			return self._right.evaluate(variables)