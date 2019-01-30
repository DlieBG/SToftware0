from functions import derivative
from functions import integral
from sympy import symbols

print("Willkommen bei SToftware0 by bschwering & ftuente")

print("Bitte gib eine Aufgabe ein! (Bsp.: 1. Ableitung von x**2)")
keyinput = input()

derivative.hook(keyinput)
integral.hook(keyinput)