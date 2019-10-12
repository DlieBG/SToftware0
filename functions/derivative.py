from sympy import *


def hook():
    return ["ableitung", "ableiten", "derivative"]


def getComponents(term, parts):

    level = "1"

    for part in parts:
        if part.endswith("."):
            level = part.split('.')[0]
            level = level

    return derivative(term, level)


def derivative(term, level):
    x = symbols('x')
    init_printing()
    out = diff(term, x, level)
    return output(out, term, int(level))


def output(out, term, level):
    print("\nDie "+str(level)+". Ableitung von "+str(term)+" ist: \n"+str(out))
    return "\n"+str(level)+". Ableitung: $$"+str(latex(out))+"$$"
