from Peekable import Peekable, peek
from newsplit import new_split_iter

def to_postfix (expr):
	return postfix_sum(Peekable(new_split_iter(expr)))