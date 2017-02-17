#exec(open("test.py").read())
from evalpostfix import eval_postfix
from infixtoiter import to_postfix
from peekable import Peekable, peek
from linkedlist import LinkedList

expr = "((1 + 2) / 3) -1"

post = to_postfix(expr)

print (eval_postfix(post))