#exec(open("evalpostfix.py").read())
from vartree import VarTree
from linkedlist import LinkedList
from peekable import Peekable, peek

def eval_postfix (iter):

	s = LinkedList() 		#s = stack
	t = VarTree()			#t = tree
	
	for token in iter:
		if (str(token)).isalnum():
			s.push(token)

		elif token == '=':
			val = s.pop()
			if not (str(val)).isdigit():		#allows assigning one variable to another
				val = t.lookup(val)				#if it finds a variable, grabs its value from the tree
			var = s.pop()
			t.assign( str(var), val)
			s.push(var)

		else:
			right = s.pop()
			left = s.pop()
			s.push(eval( str(left) + token + str(right) ))

			
	#the solution should be the only value in the stack
	sol = s.pop()
	if not (str(sol)).isdigit():
		sol = t.lookup(sol)
	return int(sol)
	
	
