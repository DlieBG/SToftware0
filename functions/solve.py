from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def hook(keyinput):
    if ("löse" in keyinput.lower() or "lösen" in keyinput.lower() or "gleichung" in keyinput.lower() or "solve" in keyinput.lower() or "solver" in keyinput.lower()) and "=" in keyinput:
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
            left = part.split("=")[0]
            right = part.split("=")[1]
    
    if term is not "" and left is not "" and right is not "":
        return solves(term, left, right)
    else:
        print("Fehler")
        return "Fehler"
        
def solves(term, left, right):
    x = symbols('x')
    init_printing(use_unicode=True)
    out = solveset(Eq(parse_expr(left), parse_expr(right)), x)
    return output(out, term)

def output(out, term):
    print("Die Lösungsmenge des Terms "+term+" ist: \nx="+str(out))
    return "\nLösungsmenge: $$x="+str(latex(out))+"$$"