from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def hook(keyinput):
    if "x" in keyinput and "exit" not in keyinput.lower() and keyinput is not "":
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part:
            term = part
            term = term.replace("y=", "")
            term = term.replace("f(x)=", "")

    if term is not "":
        return simple(term)
        
def simple(term):
    out = sympify(parse_expr(term))
    return output(out)

def output(out):
    print(str(out))
    return "\nEingabe: $$"+str(latex(out))+"$$"
