from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def hook(keyinput):
    if " " not in keyinput and "exit" not in keyinput.lower() and keyinput is not "":
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    simple(keyinput)
        
def simple(term):
    out = sympify(term)
    return output(out)

def output(out):
    print(str(out))
    return "$$x="+latex(str(out))+"$$"
