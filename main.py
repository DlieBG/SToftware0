from functions import derivative
from sympy import symbols

print("Willkommen bei SToftware0 by bschwering & ftuente")

print("Bitte gib eine Aufgabe ein! (Bsp.: 1. Ableitung von x**2)")
keyinput = input();


if "ableitung" in keyinput.lower():
    x=symbols('x')
    if len(keyinput.split(' '))>3:
        print("\nDie "+keyinput.split(' ')[0]+" Ableitung von "+keyinput.split(' ')[3]+" ist:")
        print(derivative.derivative(keyinput.split(' ')[3], keyinput.split(' ')[0].split('.')[0]))
    else:
        print("\nDie 1. Ableitung von "+keyinput.split(' ')[2]+" ist:")
        print(derivative.derivative(keyinput.split(' ')[2], 1))