from sympy import *

def hook(keyinput):
    if "chicago" in keyinput.lower():
        return "Ich komm immer klar auf n Chicago!"
    if "hello there" in keyinput.lower():
        return "General Kenobi!"
    return ""
