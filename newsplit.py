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
		
		if expr[pos].isdigit() == False:

			#the only non-digits in the expression should be + - * / ( ) so they are yielded as they are
			yield (expr[pos])
			pos += 1

		else:
			
			#use string addition to add the digits of the number together, then yield that number as an int. reset the number string after
			while expr[pos].isdigit():
				
				num += expr[pos]
				pos += 1
		
			yield (int(num))
			num = ""

	yield ";"