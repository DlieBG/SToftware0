from sympy import *

def hook(keyinput):
    #Keywords definieren
    if "schach" in keyinput:
        return output(keyinput)
    return ""

def output(keyinput):
    print("Kamelrechner ist nur Online verfügbar!")
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/chess.html'>"
