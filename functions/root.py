from sympy import *


def hook():
    return ["nullstelle", "nullstellen", "root", "roots"]


def getComponents(term):
    return roots(term)


def roots(term):
    x = symbols('x')
    init_printing()
    out = solve(term, x)
    return output(out, term)


def output(out, term):
    print("\nDie Nullstellen von "+term+" sind: \nx="+str(out))
    return "\nNullstellen: $$x="+str(latex(out))+"$$"
