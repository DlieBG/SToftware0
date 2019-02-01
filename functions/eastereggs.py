from sympy import *

def hook(keyinput):
    if "chicago" in keyinput.lower():
        print("Ich komm immer klar auf n Chicago!")
        return "Ich komm immer klar auf n Chicago!"
    if "hello there" in keyinput.lower():
        print("General Kenobi!")
        return "General Kenobi!"
    if "benedikt" in keyinput.lower():
        print("Benedikt Schwering\n")
        return "Benedikt Schwering<br>CEO von Schwering Software und SToftware<br>Lead Programmer von SToftware0<br>Technischer Informatiker"
    if "florian" in keyinput.lower():
        print("Florian Tünte\n")
        return "Florian T&uuml;nte<br>CFO von SToftware<br>Programmer von SToftware0<br>Informatiker"
    if "tarik" in keyinput.lower():
        print("Tarik Krämer\n")
        return "Tarik Kr&auml;mer<br>Designer bei SToftware"
    return ""
