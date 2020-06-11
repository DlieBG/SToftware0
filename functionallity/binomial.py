from sympy import *
from sympy import binomial


def hook():
    return ["ueber"]

def needsterm():
    return False

def getComponents(parts):

    n = -1
    k = -1

    for part in parts:
        if part.isdigit():
            if n is -1:
                n = int(part)
            elif k is -1:
                k = int(part)

    if k is not -1 and n is not -1:
        return nueK(n, k)


def nueK(n, k):
    out = binomial(n, k)
    return output(out, n, k)


def output(out, n, k):
    print("\n"+str(n)+" über "+str(k)+" ist: \n"+str(out))
    return "\nEingabe: $${"+str(n)+"\\choose "+str(k)+"}$$\nBinomialverteilung: $$"+str(latex(out))+"$$"
