from peekable import Peekable, peek
from newsplit import new_split_iter

def eval_infix_factor(iterator):
    if peek(iterator) == '(':
        next(iterator)
        bass = eval_infix_sum(iterator)
        next(iterator)
        return bass
    return int(next(iterator))

"""evaluate sum expression (zero or more additions or subtractions), using an iterator"""

def eval_infix_sum(iterator):
    bass = eval_infix_product(iterator)
    while peek(iterator) == '+' or peek(iterator) == '-':
        if peek(iterator) == '-':
            next(iterator)
            bass = bass - eval_infix_product(iterator)
        elif peek(iterator) == '+':
            next(iterator)
            bass = bass + eval_infix_product(iterator)
    return bass

def eval_infix_product(iterator):
    bass = eval_infix_factor(iterator)
    while peek(iterator) == '*' or peek(iterator) == '/' or peek(iterator) == '%' :
        if peek(iterator) == '*':
            next(iterator)
            bass = bass* eval_infix_factor(iterator)
        elif peek(iterator) == '/':
            next(iterator)
            bass = bass / eval_infix_factor(iterator)
        elif peek(iterator) == '%':
            next(iterator)
            bass = bass % eval_infix_factor(iterator)
    return bass

def eval_infix_iter(iterator):
     return eval_infix_sum(Peekable(iterator))
    
def eval_infix(expr):
     return eval_infix_iter(new_split_iter(expr))   # make a list, and append

if __name__ == "__main__":
    print ( eval_infix("5 ") )
    print ( eval_infix("15 ") )
    print ( eval_infix( " 2 * 3 + 1  " ) )
    print ( eval_infix( " 2 + 3 * 1" ) )







