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
            if "=" in term:
                term = term.split("=")[1]
            term = term.replace("y=", "")
            term = term.replace("f(x)=", "")
        if part.isdigit() and a is "":
            a = part
        elif part.isdigit() and a is not "" and b is "":
            b = part
    
    if term is not "":
        return integral(term, a, b)
    else:
        print("Es konnte kein Term gefunden werden")
        return "Es konnte kein Term gefunden werden"
        
def integral(term, a, b):
    x = symbols('x')
    init_printing(use_unicode=True)
    if a is "" or b is "":
        out = integrate(term, x)
    else:
        out = integrate(term, (x, a, b))
    return output(out, term, a, b)

def output(out, term, a, b):
    if a is "" or b is "":
        print("\nDie Stammfunktion von "+term+" ist: \n"+str(out)+"+c")
        return "\nStammfunktion: $$"+str(latex(out))+"+c$$"
    else:
        print("\nDas Integral von "+term+", im Bereich von "+a+" bis "+b+" ist: \n"+str(out))
        return "\nIntegral von "+a+" bis "+b+": $$"+str(latex(out))+"$$"
