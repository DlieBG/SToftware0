from functions import derivative
from functions import integral
from sympy import symbols
import os

print("Willkommen bei SToftware0 by bschwering & ftuente")


def main():
    print("\n\nBitte gib eine Aufgabe ein! (Bsp.: 1. Ableitung von x**2)")
    keyinput = input()

    derivative.hook(keyinput)
    integral.hook(keyinput)
    main()

main()