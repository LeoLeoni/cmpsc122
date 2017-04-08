#exec(open("infixtotree.py").read())
from peekable import Peekable, peek
from newsplit import new_split_iter
from exprtree import Value, Var, Oper, Cond, Funct

#	precedence:		assign > conditional > relational > addition > product > parens
#	similar alg to infixtoiter from previous except in tree form
#	left and right nodes are subtrees instead of just values

def tree_assign(iter):
	"""Handles variable assignments"""

	left = tree_cond(iter)

	while peek(iter) == '=':
		sign = next(iter)
		right = tree_cond(iter)
		left = Oper(left, sign, right)
	return left


def tree_cond(iter):
	"""Handles conditional statements"""

	left = tree_relate(iter)	#the test condition subtree
	while peek(iter) == '?':
		next(iter)				#passes over the ?
		t = tree_cond(iter)		#the true expression subtree
		next(iter)				#passses over the :
		f = tree_cond(iter)		#the false expression subtree
		left = Cond(left, t, f)
	return left

def tree_relate(iter):
	"""Handles relational expressions"""

	left = tree_sum(iter)

	while peek(iter) in ["==", "!=", "<=", ">=", '>', '<']:
		sign = next(iter)
		right = tree_sum(iter)
		left = Oper(left, sign, right)
	return left

def tree_sum(iter):
	"""Handles addition"""

	left = tree_prod(iter)

	while peek(iter) == '+' or peek(iter) == '-':
		sign = next(iter)
		right = tree_prod(iter)
		left = Oper(left, sign, right)
	return left

def tree_prod(iter):
	"""Handles multiplication and division"""

	left = tree_factor(iter)

	while peek(iter) in ['*', '/', '%']:
		sign = next(iter)
		right = tree_factor(iter)
		left = Oper(left, sign, right)
	return left


def tree_factor(iter):
	"""Handles parentheses"""

	next = str(next(iter))
	if next == '(':
		next(iter)				
		ans = tree_assign(iter)	#recursively makes a new expr subtree for the contents of the parens
		next(iter)				#passes over )
		return ans
	
	elif next.isdigit():
		return Value(next(iter))

	elif peek(iter) == '(':
		args = []
		while peek(iter) != ')':
			next(iter)
			args.append(tree_assign(iter))
		next(iter)
		return Funct(nxt, args)

	elif next.isalpha():
		return Var(next(iter))


def to_expr_tree(expr):
	return tree_assign(Peekable(new_split_iter(expr)))

