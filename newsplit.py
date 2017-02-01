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

			yield (expr[pos])
			pos += 1

		else:
			
			while expr[pos].isdigit():

				num += expr[pos]
				pos += 1
		
			yield (int(num))
			num = ""