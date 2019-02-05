from sympy import *

def hook(keyinput):
    if "hilfe" in keyinput.lower() or "help" in keyinput.lower() or "wiki" in keyinput.lower() or keyinput is "":
        print("\nGib eine Aufgabe ein!\n\nBeispiele:\n2. Ableitung von x^2\nGleichung lösen: x^3=21*x\nKurvendiskussion 2*x^3+x^2")
        return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions.html'>"
    if "chicago" in keyinput.lower():
        print("Ich komm immer klar auf n Chicago!")
        return "<h3>Ich komm immer klar auf n Chicago!</h3>"
    if "hello there" in keyinput.lower():
        print("General Kenobi!")
        return "<h3>General Kenobi!</h3>"
    if "moped" in keyinput.lower():
        print("SOOS!")
        return "<h2>SOOS!</h2>"
    if "benedikt" in keyinput.lower() or "ceo" in keyinput.lower() or "programmier" in keyinput.lower() or "erfinder" in keyinput.lower() "erfunden" in keyinput.lower() or "entwickelt" in keyinput.lower() or:
        print("Benedikt Schwering\n")
        return "<h3>Benedikt Schwering<br>CEO von Schwering Software und SToftware<br>Lead Programmer von SToftware0<br>Technischer Informatiker</h3>"
    if "florian" in keyinput.lower():
        print("Florian Tünte\n")
        return "<h3>Florian T&uuml;nte<br>CFO von SToftware<br>Programmer von SToftware0<br>Informatiker</h3>"
    return ""
