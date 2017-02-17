#exec(open("infixtoiter.py").read())
from peekable import Peekable, peek
from newsplit import new_split_iter

def to_postfix (expr):
	return postfix_sum(Peekable(new_split_iter(expr)))

def postfix_sum (iterator):

	yield from postfix_product(iterator)
	
	while peek(iterator) == '+' or peek(iterator) == '-':
		sign = next(iterator)	#should be an operator sign
		yield from postfix_product(iterator)
		yield sign

def postfix_product (iterator):

	yield from postfix_factor(iterator)

	while peek(iterator) == '*' or peek(iterator) == '/' or peek(iterator) =='%':
		sign = next(iterator)		#should be an operator sign
		yield from postfix_factor(iterator)
		yield sign

def postfix_factor (iterator):

	if peek(iterator) == '(':
		next(iterator)		#passes over the (
		yield from postfix_sum(iterator)
		next(iterator)		#passes over the )

	else:	#yields all numbers before any of the "yield sign" lines run
			#recursion should hopefully ensure all of the operator signs are kept in memory?
		yield next(iterator)