from sympy import *

def hook(keyinput):
    if ("löse" in keyinput.lower() or "lösen" in keyinput.lower() or "gleichung" in keyinput.lower()) and "=" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""
    left = ""
    right = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "=" in part:
            term = part
            left = part.split("=")[0]
            right = part.split("=")[1]
    
    if term is not "":
        return solves(term, left, right)
    else:
        print("Fehler")
        return "Fehler"
        
def solves(term, left, right):
    x = symbols('x')
    init_printing(use_unicode=True)
    out = solve(Eq(left, right), x)
    return output(out, term)

def output(out, term):
    print("Die Lösungsmenge des Terms "+term+" ist: \nx="+str(out))
    return "Die Lösungsmenge des Terms "+term+" ist: $$x="+str(latex(out))+"$$"