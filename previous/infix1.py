#exec in python 3 shell: exec(open("infix1.py").read())

def eval_infix_sum(expr, pos):
	"""evaluate a sum expression (zero or more additions and subtractions)"""

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
	#this function figures out whats inside the parentheses, creates a new string for that part and evaluates that substring

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

	return expr

def eval_infix(expr):       

	expr = eval_infix_list(expr.split())
	return expr

def eval_infix_list(expr):

	#adds a semicolon making the string easier to work with
	if expr[-1] != ';':
		expr += ';'
	
	#i tried using a "for pos in range" thing and it didnt work so im doing this. 
	while ('(' in expr) or (')' in expr):
		pos = 0
		while not(expr[pos] == '('):
			pos += 1

		expr = eval_infix_factor(expr, pos)
	
	#does all of the multiplcation and division operations until there are no more * or / signs
	while ('*' in expr) or ('/' in expr):
		pos = 0
		while not((expr[pos] == '*') or (expr[pos] == '/')):
			pos += 1

		expr = eval_infix_product (expr, pos)


	#does all of the add/sub operations until there are no more + or - signs
	while ('+' in expr) or ('-' in expr):
		pos = 0
		while not((expr[pos] == '+') or (expr[pos] == '-')):
			 pos += 1

		expr = eval_infix_sum (expr, pos)

	return (expr[0])