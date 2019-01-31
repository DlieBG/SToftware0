from sympy import *

def hook(keyinput):
    #Keywords definieren
    if "extremstellen" in keyinput.lower() or "extrempunkte" in keyinput.lower() or "maxima" in keyinput.lower() or "minima" in keyinput.lower():
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    #Variablen

    parts = keyinput.split(' ')
    for part in parts:
        #Teile den Variablen zuordnen
    
    if  is not "": #Abbruchbedingung
        return functionX()
    else:
        print("Fehler")
        return "Fehler"
        
def functionX():
    #Berechnung der 
    return output(out, term)

def output(out, term):
    #Ausgabe der Werte