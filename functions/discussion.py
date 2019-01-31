from sympy import *

def hook(keyinput):
    #Keywords definieren
    if "kurvendiskussion" in keyinput.lower() or "diskussion" in keyinput.lower() or "discuss" in keyinput.lower():
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