from sympy import *

def hook(keyinput):
    if "extremstellen" in keyinput.lower() or "extrempunkte" in keyinput.lower() or "maxima" in keyinput.lower() or "minima" in keyinput.lower():
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part and "maxima" not in part:
            term = part
            if "=" in term:
                term = term.split("=")[1]
            term = term.replace("y=", "")
            term = term.replace("f(x)=", "")
    
    if term is not "":
        return extrems(term)
    else:
        print("Fehler")
        return "Fehler"
        
def extrems(term):
    x = symbols('x')
    init_printing(use_unicode=True)
    deriv = diff(term, x, 1)
    out = solve(deriv, x)
    return output(out, term)

def output(out, term):
    print("\nDie Extremstellen von "+term+" sind: \nx="+str(out))
    return "\nExtremstellen: $$x="+str(latex(out))+"$$"
