#exec(open("infix2.py").read())
#parentheses dont work yet. had to completely redo the algorithm i used in homework 1 and couldn't get it to work

from peekable import Peekable, peek
from newsplit import new_split_iter


def eval_infix_sum(iterator):
	"""evaluate a sum expression (zero or more additions and subtractions)"""

	#pretty straightforward. calls the product funtion for next numbers but will do productsa when needed.
	ans = eval_infix_product(iterator)

	while peek(iterator) != ';':

		if peek(iterator) == '+':
			next(iterator)
			ans += eval_infix_product(iterator)

		elif peek(iterator) == '-':
			next(iterator)
			ans -= eval_infix_product(iterator)


	return(ans)
	

def eval_infix_product(iterator):
	"""evaluate a product expression (zero or more multiplications/divisions)"""

	#if there are no * or / signs this funtion will simply return the next number
	#-that way whenever it is called it will return the products and sums if there are any
	#-and the next number in the list if not

	
	ans = eval_infix_factor(iterator)
	while peek(iterator) == "*" or peek(iterator) == '/':

		if peek(iterator) == '*':
			next(iterator)
			ans *= eval_infix_factor(iterator)

		elif peek(iterator) == '/':
			next(iterator)
			ans //= eval_infix_factor(iterator)

	return (ans)

def eval_infix_factor(iterator):
	#haven't quite got this far yet
	#i have the implementation in the right place but i couldn't figure out the algorithm in time to submit the assignment

	ans = next(iterator)

	return (ans)


def eval_infix_iter(iterator):
	"""evaluate an expression, given an iterator to its tokens"""
	return eval_infix_sum(Peekable(iterator))


def eval_infix(expr):       
	"""accept a character string, split it into tokens, then evaluate"""
	return eval_infix_iter(new_split_iter(expr))