from sympy import *

def hook(keyinput):
    if "wendestelle" in keyinput.lower() or "wendepunkt" in keyinput.lower() or "wende" in keyinput.lower() or "turn" in keyinput.lower():
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
        return turns(term)
    else:
        print("Fehler")
        return "Fehler"
        
def turns(term):
    x = symbols('x')
    init_printing(use_unicode=True)
    deriv = diff(term, x, 2)
    out = solve(deriv, x)
    return output(out, term)

def output(out, term):
    print("\nDie Wendestellen von "+term+" sind: \nx="+str(out))
    return "\nWendestellen: $$x="+str(latex(out))+"$$"
