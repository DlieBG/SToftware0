from sympy import *


def hook():
    return ["nullstelle", "nullstellen", "root", "roots"]

def needsterm():
    return True

def getComponents(term,parts):
    return findroots(term)


def findroots(term):
    x = symbols('x')
    init_printing()
    out = solve(term, x)
    return output(out, term)


def output(out, term):
    print("\nDie Nullstellen von "+term+" sind: \nx="+str(out))
    return "\nNullstellen: $$x="+str(latex(out))+"$$"
