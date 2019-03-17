from sympy import *
from mpmath import *

def hook(keyinput):
    if "nullstelle" in keyinput or "nullstellen" in keyinput or "root" in keyinput or "roots" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part:
            term = part
            if "=" in term:
                term = term.split("=")[1]
            term = term.replace("y=", "")
            term = term.replace("f(x)=", "")
    
    if term is not "":
        return rootss(term)
    else:
        print("Fehler")
        return "Fehler"
        
def rootss(term):
    x = symbols('x')
    init_printing()
    out = solve(term, x)
    return output(out, term)

def output(out, term):
    print("\nDie Nullstellen von "+term+" sind: \nx="+str(out))
    return "\nNullstellen: $$x="+str(latex(out))+"$$"
