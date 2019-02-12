from sympy import *

def hook(keyinput):
    #Keywords definieren
    if "kamel" in keyinput:
        return output(keyinput)
    return ""

def output(keyinput):
    print("Kamelrechner ist nur Online verfügbar!")
    return()
