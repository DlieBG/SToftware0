from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def hook(keyinput):
    if ("loese" in keyinput or "gleichung" in keyinput or "solve" in keyinput or "solver" in keyinput) and "=" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""
    left = ""
    right = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "=" in part:
            term = part
            if "=" in term:
                term = term.split("=")[1]
            left = part.split("=")[0]
            right = part.split("=")[1]

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
    print("\nDie Lösungsmenge des Terms "+term+" ist: \nx="+str(out))
    return "\nLösungsmenge: $$x="+str(latex(out))+"$$"
