#exec(open("test.py").read())
from evalpostfix import eval_postfix
from infixtoiter import to_postfix

def test (expr):
    print (expr, " = ", eval_postfix(to_postfix(expr)) )