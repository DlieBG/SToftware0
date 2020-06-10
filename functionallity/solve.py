from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def hook():
    return ["loese", "gleichung", "solve", "solver"]


def getComponents(term):
    left = term.split("=")[0]
    right = term.split("=")[1]

    if term is not "" and left is not "" and right is not "":
        return solves(term, left, right)
    else:
        print("Fehler")
        return "Fehler"


def solves(term, left, right):
    x = symbols('x')
    init_printing()
    out = solveset(Eq(parse_expr(left), parse_expr(right)), x)
    return output(out, term)


def output(out, term):
    print("\nDie Lösungsmenge des Terms "+str(term)+" ist: \nx="+str(out))
    return "\nLösungsmenge: $$x="+str(latex(out))+"$$"
