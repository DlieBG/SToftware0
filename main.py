import sympy
import os
import importlib
from os import walk
from functions import *

def main():
    print("\n\nBitte gib eine Query ein:")
    keyinput = input()
    keyinput = keyinput.lower()
    keyinput = keyinput.replace("^", "**")
    keyinput = keyinput.replace("f(x)=", "")
    keyinput = keyinput.replace("y=", "")
    try:
        for function in os.listdir("functions"):
            if function[0] is not '_': 
                getattr(globals().get(function[:-3]), "hook")(keyinput)
    except:
        print("Entweder DU bist schuld oder das Programm ist schuld")
    finally:
        if "exit" not in keyinput:
            main()

print("Willommen bei SToftware0!\n\nhttps://benedikt-schwering.de/SToftware0\nBenedikt Schwering und Florian Tünte")
main()