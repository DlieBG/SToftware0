from sympy import *
from sympy import binomial


def hook():
    return ["ueber", "über"]


def needsterm():
    return False


def getComponents(parts):

    n = -1
    k = -1

    for part in parts:
        if part.isdigit():
            if n == -1:
                n = int(part)
            elif k == -1:
                k = int(part)

    if k != -1 and n != -1:
        return nueK(n, k)


def nueK(n, k):
    out = binomial(n, k)
    return output(out, n, k)


def output(out, n, k):
    print(""+str(n)+" über "+str(k)+" ist: \n"+str(out))
    return "\nEingabe: $${"+str(n)+"\\choose "+str(k)+"}$$\nBinomialverteilung: $$"+str(latex(out))+"$$"
