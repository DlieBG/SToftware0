from sympy import *

def hook(keyinput):
    #Keywords definieren
    if "kamel" in keyinput:
        return output(keyinput)
    return ""

def output(keyinput):
    print("Kamelrechner ist nur Online verfügbar!")
    return "<meta http-equiv='refresh' content='0; URL=https://benedikt-schwering.de/SToftware0/html/mobile/functions/kamel.html'>"
