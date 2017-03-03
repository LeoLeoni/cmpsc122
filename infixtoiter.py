#exec(open("infixtoiter.py").read())
from peekable import Peekable, peek
from newsplit import new_split_iter

def to_postfix (expr):
	return postfix_equals(Peekable(new_split_iter(expr)))

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
		yield from postfix_equals(iterator)
		next(iterator)		#passes over the )

	else:
		yield next(iterator)

def postfix_equals (iterator):

	yield from postfix_sum

	while peek(iterator) == '=':
		sign = next(iterator)
		yield from postfix_sum(iterator)
		yield sign
