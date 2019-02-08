from sympy import symbols
import os

from functions import eastereggs
from functions import derivative
from functions import integral
from functions import root
from functions import solve
from functions import extrems
from functions import simple
from functions import discussion
from functions import turns
from functions import plotcli
print("Willkommen bei SToftware0 by bschwering & ftuente")


def main():
    print("\n\nBitte gib eine Aufgabe ein! (Bsp.: 1. Ableitung von x**2)")
    keyinput = input()
    keyinput = keyinput.lower()
    keyinput = keyinput.replace("^", "**")
    keyinput = keyinput.replace("f(x)=", "")
    keyinput = keyinput.replace("y=", "")
    try:
        simple.hook(keyinput)
        discussion.hook(keyinput)
        eastereggs.hook(keyinput)
        derivative.hook(keyinput)
        integral.hook(keyinput)
        root.hook(keyinput)
        extrems.hook(keyinput)
        turns.hook(keyinput)
        solve.hook(keyinput)
        plotcli.hook(keyinput)
    except:
        print("Entweder DU bist schuld oder das Programm ist schuld")
    finally:
        if "exit" not in keyinput:
            main()

main()
