from sympy import *

def hook(keyinput):
    #Keywords definieren
    if "Schach" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):
    return output()

def output():
    print("Bitte benutze die Onlineversion!")
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/chess.html'>"