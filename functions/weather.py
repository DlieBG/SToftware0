from sympy import *

def hook(keyinput):
    if "wetter" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    ort = ""

    parts = keyinput.split(' ')
    for part in parts:
        #Teile den Variablen zuordnen

    if  is not "": #Abbruchbedingung
        return output(ort)
    else:
        print("Fehler")
        return "Fehler"

def output(ort):
    print("Wetter ist nur Online verfügbar.")
