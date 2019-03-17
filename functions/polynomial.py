from sympy import *

def hook(keyinput):
    if "polinom" in keyinput and ("division" in keyinput or "dividi" in keyinput):
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    a = ""
    b = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "/" in part:#TODO optimize for / in a or b  Maybe tomorrow XD
            a = part.split("/")[0]
            b = part.split("/")[1]

    if a is not "" and b is not "":
        return polinomdiv(a, b)
    else:
        print("Fehler")
        return "Fehler"

def polinomdiv(a, b):
    x = symbols('x')
    init_printing()
    out, g = div(a, b, x)
    return output(out, a, b)

def output(out, a, b):
    print("\nPolinomdivision von "+str(a)+"/"+str(b)+" ist: \n"+str(out))
    return "\nPolinomdivision: $$"+str(latex(out))+"$$"
