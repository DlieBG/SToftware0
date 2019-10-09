from sympy import *

def hook(keyinput):
    if "stammfunktion" in keyinput or "integral" in keyinput or "aufleitung" in keyinput or "aufleiten" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""
    a = ""
    b = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part:
            term = part
        if isfloat(part) and a is "":
            a = float(part)
        elif isfloat(part) and a is not "" and b is "":
            b = float(part)
    
    if term is not "":
        return integral(term, a, b)
    else:
        print("Es konnte kein Term gefunden werden")
        return "Es konnte kein Term gefunden werden"

def isfloat(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def integral(term, a, b):
    a=float(a)
    b=float(b)
    x = symbols('x')
    init_printing()
    if a is "" or b is "":
        out = integrate(term, x)
    else:
        out = integrate(term, (x, a, b))
    return output(out, term, a, b)

def output(out, term, a, b):
    if a is "" or b is "":
        print("\nDie Stammfunktion von "+str(term)+" ist: \n"+str(out)+"+c")
        return "\nStammfunktion: $$"+str(latex(out))+"+c$$"
    else:
        print("\nDas Integral von "+str(term)+", im Bereich von "+str(a)+" bis "+str(b)+" ist: \n"+str(out))
        return "\nIntegral von "+str(a)+" bis "+str(b)+": $$"+str(latex(out))+"$$"
