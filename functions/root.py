from sympy import *
from mpmath import *

def hook(keyinput):
    if "nullstelle" in keyinput.lower() or "nullstellen" in keyinput.lower() or "root" in keyinput.lower() or "roots" in keyinput.lower():
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
        return rootss(term)
    else:
        print("Fehler")
        return "Fehler"
        
def rootss(term):
    x = symbols('x')
    init_printing(use_unicode=True)
    out = solve(term, x)
    return output(out, term)

def output(out, term):
    print("Die Nullstellen von "+term+" sind: \nx="+str(out))
    return "Die Nullstellen von "+term+" sind: $$x="+str(latex(out))+"$$"