from sympy import *
from sympy import binomial

def hook(keyinput):
    #Keywords definieren
    if "ueber" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    n = ""
    k = ""

    parts = keyinput.split(' ')
    for part in parts:
        if part.isdigit():
            if n is "":
                n = int(part)
            else:
                k = int(part)


    if k is not "" and n is not "": #Abbruchbedingung
        return nT(n, k)
    else:
        print("Fehler")
        return "Fehler"

def nT(n, k):
    out = binomial(n, k)
    return output(out, n, k)

def output(out, n, k):
    print("\n"+n+" über "+k+" ist: \n"+str(out))
    return "\nBinomialverteilung: "+'$$\binom{'+n+'}{'+k+'}'+str(latex(out))+"$$"