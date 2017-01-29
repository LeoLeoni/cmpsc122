#exec(open("infix1.py").read())

def eval_infix_sum(expr, pos):
	"""evaluate a sum expression (zero or more additions and subtractions)"""

	#pos SHOULD be on the operator sign		

	#replaces the first value with the sum/difference
	if (expr[pos] == '+'):

		expr[pos-1] = int(expr[pos-1]) + int(expr[pos+1])     

	elif (expr[pos] == '-'):
		
		expr[pos-1] = int(expr[pos-1]) - int(expr[pos+1])

	#deletes the operator sign and the second number
	del expr[pos : pos+2]

	return(expr)    


def eval_infix_product(expr, pos):
	"""evaluate a product expression (zero or more multiplications/divisions)"""

	#pos SHOULD be on the operator sign		

	#replaces the first value with the product
	if (expr[pos] == '*'):

		expr[pos-1] = int(expr[pos-1]) * int(expr[pos+1])     

	elif (expr[pos] == '/'):
		
		expr[pos-1] = int(expr[pos-1]) // int(expr[pos+1])

	#deletes the operator sign and the second number
	del expr[pos : pos+2]

	return(expr)

def eval_infix_factor(expr, pos):
	"""evaluate a factor (number or parenthesized sub-expression)"""

	#figures out whats inside the parentheses, creates a new string for that part and then evaluates that substring

	#the number of open/closed parentheses. this is necessary to make sure nested parentheses work
	openparen = 1
	closeparen = 0
	#position for the substring that will be evaluated
	endpos = pos

	#breaks when the currently open parentheses are closed
	while (openparen != closeparen):

		endpos += 1

		if expr[endpos] == '(':
			openparen += 1
		elif expr[endpos] == ")":
			closeparen += 1

	#gather the contents of the brackets into a new list which will be evaluated. should work with nested parentheses
	subexpr = expr[(pos+1) : endpos]

	ans = eval_infix_list(subexpr)

	expr[pos] = ans
	del expr[pos+1 : endpos+1]

	return (expr)

def eval_infix(expr):       

	expr = eval_infix_list(expr.split())

	return expr

def eval_infix_list(expr):
	
	#adds a semicolon making the string easier to work with	
	expr.append(';')
	
	#each loop runs through the list, evaluating parts of expr in order of operations
	#the first loop evaluates all parenthesized expressions
	pos = 0
	while expr[pos] != ';':

		if expr[pos] == '(':

			expr = eval_infix_factor(expr, pos)

		pos += 1

	#then all the multiplications/divisions
	pos = 0
	while expr[pos] != ';':

		if expr[pos] == '*' or expr[pos] == '/':

			expr = eval_infix_product(expr, pos)
			pos -= 1
		
		pos += 1
	
	#then all the additions/subtractions
	pos = 0
	while expr[pos] != ';':

		if expr[pos] == '+' or expr[pos] == '-':

			expr = eval_infix_sum(expr, pos)
			pos -= 1
	
		pos += 1

	#there should be nothing left other than the solution at position 0
	return (expr[0])