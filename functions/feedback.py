from sympy import *

def hook(keyinput):
    #Keywords definieren
    if "feedback" in keyinput or "bewertung" in keyinput or "rezension" in keyinput or "fehler" in keyinput:
        return output(keyinput)
    return ""

def output(keyinput):
    print("Bewertung ist nur Online verfügbar!\nWenn Sie so krass sind, dass sie die Kommandozeilenfunktion nutzen, können Sie uns Ihre Ideen einfach auf Github mitteilen!")
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/bewertung.php'>"
