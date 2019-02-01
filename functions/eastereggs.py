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
        return "Benedikt Schwering\nCEO von Schwering Software und SToftware\nLead Programmer von SToftware0\nTechnischer Informatiker\n"
    return ""
