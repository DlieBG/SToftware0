from sympy import *

def hook(keyinput):
    if "chicago" in keyinput.lower():
        getComponents(keyinput)

def getComponents(keyinput):

    out = "Ich komm immer klar auf n Chicago!"
    output(out)
        
#Berechnung der Werte

def output(out):
    print(out)