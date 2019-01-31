from sympy import *

def hook(keyinput):
    if "chicago" in keyinput.lower():
        print("Ich komm immer klar auf n Chicago!")
        return "$$Ich komm immer klar auf n Chicago!$$"
    if "hello there" in keyinput.lower():
        print("General Kenobi!")
        return "$$General Kenobi!$$"
    return ""
