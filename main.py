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
from functions import kamel
from functions import feedback
from functions import polynomial
from functions import weather
from functions import binomial

print("Willkommen bei SToftware0 by bschwering & ftuente\n\nBesuche doch mal die Website benedikt-schwering.de/SToftware0\n")

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
        kamel.hook(keyinput)
        feedback.hook(keyinput)
        polynomial.hook(keyinput)
        weather.hook(keyinput)
        binomial.hook(keyinput)
    except:
        print("Entweder DU bist schuld oder das Programm ist schuld")
    finally:
        if "exit" not in keyinput:
            main()

main()
