#exec(open("newsplit.py").read())

def new_split_iter( expr ):
	"""divide a character string into individual tokens, which need not be separated by spaces (but can be!) 
	also, the results are returned in a manner similar to iterator instead of a new data structure
	"""
	#takes out spaces in case there are spaces
	expr = expr.replace(" ", "")
	expr += ";"
	pos = 0
	num = ""    #initialized as str to make use of string addition

	while expr[pos] != ";":

		if not expr[pos].isalnum():
			#the only non-alnums in the expression should be + - * / ( ) = so they are yielded as they are
			yield expr[pos]
			pos += 1

		elif not expr[pos].isdigit():
			#support for variables that start with a letter
			while expr[pos].isalnum():	#will not work if the variable name starts with a number
				num += expr[pos]
				pos += 1
			yield num
			num = ""

		else:
			#use string addition to add the digits of the number together, then yield that number as an int. reset the number string after
			while expr[pos].isdigit():
				num += expr[pos]
				pos += 1
		
			yield int(num)
			num = ""

	yield ";"