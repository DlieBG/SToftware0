from sympy import *


def hook():
    return ["polinomdivision", "polinomdividi"]


def needsterm():
    return False


def getComponents(parts):

    a = ""
    b = ""

    for part in parts:
        if "/" in part:  # TODO optimize for / in a or b  Maybe tomorrow XD
            a = part.split("/")[0]
            b = part.split("/")[1]

    if a != "" and b != "":
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
    print("Polinomdivision von "+str(a)+"/"+str(b)+" ist: \n"+str(out))
    return "\nPolinomdivision: $$"+str(latex(out))+"$$"