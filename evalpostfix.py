#exec(open("evalpostfix.py").read())
from linkedlist import LinkedList
from peekable import Peekable, peek

def eval_postfix (iter):

	iter = Peekable (iter)
	s = LinkedList() #s = stack
	s.push(next(iter)) #first value will always be a number

	while not s.is_empty():
		
		if peek(iter) == '+':
			second = s.pop()
			s.push(s.pop() + second)

		elif peek(iter) == '-':
			second = s.pop()
			s.push(s.pop() - second)

		elif peek(iter) == '*':

		elif peek(iter) == '/':

		elif peek(iter) == '%':

		else:
			s.push(next(iter))

	
