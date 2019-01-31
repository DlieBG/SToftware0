from sympy import *

def hook(keyinput):
    if "ableitung" in keyinput.lower() or "ableiten" in keyinput.lower() or "derivative" in keyinput.lower():
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""
    level = "1"

    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part:
            term = part
            if "=" in term:
                term = term.split("=")[1]
            term = term.replace("y=", "")
            term = term.replace("f(x)=", "")
        if part.endswith("."):
            level = part.split('.')[0]
            level = level
    
    if term is not "":
        return derivative(term, level)
    else:
        print("Es konnte kein Term gefunden werden")
        
def derivative(term, level):
    x = symbols('x')
    init_printing(use_unicode=True)
    out = diff(term, x, level)
    return output(out, term, int(level))

def output(out, term, level):
    print("\nDie "+str(level)+". Ableitung von "+term+" ist: \n"+str(out))
    return "\n"+str(level)+". Ableitung: $$"+str(latex(out))+"$$"