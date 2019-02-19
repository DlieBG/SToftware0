from sympy import *

def hook(keyinput):
    if "wetter" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    ort = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "wetter" not in part:
            ort = part.replace("?", "")
            ort = ort.capitalize()

    if ort is not "": #Abbruchbedingung
        return output(ort)
    else:
        print("Fehler")
        return "Fehler"

def output(ort):
    print("Wetter für "+ort+" ist nur Online verfügbar.")
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/weather.html?"+ort+"'>"    
