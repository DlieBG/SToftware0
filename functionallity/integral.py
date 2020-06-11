from sympy import *


def hook():
    return ["stammfunktion", "integral", "aufleitung", "aufleiten", "integrate"]

def needsterm():
    return True

def getComponents(term, parts):

    a = ""
    b = ""

    for part in parts:
        if isfloat(part) and a is "":
            a = part
        elif isfloat(part) and a is not "" and b is "":
            b = part

    return integral(term, a, b)


def isfloat(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


def integral(term, a, b):
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
