from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def hook():
    return []

def needsterm():
    return True

def getComponents(term,parts):

    if "=" not in term:
        return simple(term)
    else:
        left = term.split("=")[0]
        right = term.split("=")[1]
    
        if term is not "" and left is not "" and right is not "":
            return simpleEq(left,right)
        else:
            print("Fehler")
            return "Fehler"


def simple(term):
    out = sympify(parse_expr(term))
    return output(out)


def simpleEq(left,right):
    left = sympify(parse_expr(left))
    right = sympify(parse_expr(right))
    return output2(left,right)


def output(out):
    print("\n"+str(out))
    return "\nEingabe: $$"+str(latex(out))+"$$"


def output2(left,right):
    print("\n"+str(left)+"="+str(right))
    return "\nEingabe: $$"+str(latex(left))+"="+str(latex(right))+"$$"
