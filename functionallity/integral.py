from sympy import *
from expr import *
import string

def hook():
    return ["stammfunktion", "integral", "aufleitung", "aufleiten", "integrate"]


def needsterm():
    return True


def getComponents(term, parts):

    a = ""
    b = ""

    for part in parts:
        if isTerm(part) and a == "":
            a = part
        elif isTerm(part) and a != "" and b == "":
            b = part
    print(term+a+b)
    return integral(term, a, b)


def integral(term, a, b):
    x = symbols(string.ascii_lowercase)
    init_printing()
    if a == "" or b == "":
        out = integrate(term, x)
    else:
        out = integrate(term, (x, a, b))
    return output(out, term, a, b)


def output(out, term, a, b):
    if a == "" or b == "":
        print("Die Stammfunktion von "+str(term)+" ist: \n"+str(out)+"+c")
        return "\nStammfunktion: $$"+str(latex(out))+"+c$$"
    else:
        print("Das Integral von "+str(term)+", im Bereich von " +
              str(a)+" bis "+str(b)+" ist: \n"+str(out))
        return "\nIntegral von "+str(a)+" bis "+str(b)+": $$"+str(latex(out))+"$$"
