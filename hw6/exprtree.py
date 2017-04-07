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
	def evaluate(self, variables, functions):
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
	def evaluate(self, variables, functions):
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

	def evaluate(self, variables, functions):
		#mux where cond is the selector, false = 0 and true = 1																						#this is a long return statement but it works
		return self._cond.evaluate(variables,functions) and self._true.evaluate(variables,functions) or not self._cond.evaluate(variables,functions) and self._false.evaluate(variables,functions)


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

	def evaluate(self, variables, functions):

		"""Evaluates the expression with support for relational operators."""
		if self._oper != '=':
			#eval() will return a bool given a relational oper, and a number given a arithmetic oper
			return eval(  str(self._left.evaluate(variables,functions))  +  self._oper + str(self._right.evaluate(variables,functions))  )		#needed to convert to string because python is weird
		else:
			#in this case left should always be a var name and right should always be the value being assigned to it
			variables.assign(self._left._name, self._right.evaluate(variables,functions))
			return self._right.evaluate(variables,functions)

class Funct(ExprTree):

	def __init__ (self, name, arg):
		self._name = name
		self._arg = arg

	def __iter__(self):
		yield self._name
		yield "("
		yield from self._arg
		yield ")"

	def postfix(self):
		#still not sure why this is needed to work
		pass
	
	def evaluate(self, variables, functions):
		parms, body = functions.lookup(self._name)
		newTree = VarTree()
		for i in range(0, len(parms)):
			newTree.assign(parms[i], self._arg[i].evaluate(variables, functions))
		return body.evaluate(newTree, functions)