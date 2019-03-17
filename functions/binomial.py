from sympy import *
from sympy import binomial

def hook(keyinput):
    #Keywords definieren
    if "ueber" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    n = -1
    k = -1

    parts = keyinput.split(' ')
    for part in parts:
        if part.isdigit():
            if n is -1:
                n = int(part)
            else:
                k = int(part)


    if k is not -1 and n is not -1: #Abbruchbedingung
        return nueK(n, k)
    else:
        print("Fehler")
        return "Fehler"

def nueK(n, k):
    out = binomial(n, k)
    return output(out, n, k)

def output(out, n, k):
    print("\n"+str(n)+" über "+str(k)+" ist: \n"+str(out))
    return "\nBinomialverteilung: "+str(latex(out))+"$$"