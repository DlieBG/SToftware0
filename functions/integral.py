from sympy import *

def hook(keyinput):
    if "stammfunktion" in keyinput.lower() or "integral" in keyinput.lower() or "aufleitung" in keyinput.lower() or "aufleiten" in keyinput.lower():
        getComponents(keyinput)

def getComponents(keyinput):

    term = ""
    a = ""
    b = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part:
            term = part
            term = term.replace("y=", "")
            term = term.replace("f(x)=", "")
        if part.isdigit() and a is "":
            a = part
        elif part.isdigit() and a is not "" and b is "":
            b = part
    
    if term is not "":
        integral(term, a, b)
    else:
        print("Es konnte kein Term gefunden werden")
        
def integral(term, a, b):
    x = symbols('x')
    init_printing(use_unicode=True)
    if a is "" or b is "":
        out = integrate(term, x)
    else:
        out = integrate(term, (x, a, b))
    output(out, term, a, b)

def output(out, term, a, b):
    if a is "" or b is "":
        print("\nDie Stammfunktion von "+term+" ist: \n"+str(out))
    else:
        print("\nDas Integral von "+term+", im Bereich von "+a+" bis "+b+" ist: \n"+str(out))