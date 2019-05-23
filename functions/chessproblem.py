from sympy import *
from fractions import Fraction

def hook(keyinput):
    #Keywords definieren
    if "schach" in keyinput:
        if "anfang" in keyinput:
            return anfangsmatrix()
        return output(keyinput)
    return ""

def anfangsmatrix():
    M = Matrix([
    [0,Fraction(1,5),0,0,Fraction(1,5),Fraction(1,8),0,0,0,0,0,0,0,0,0,0],
    [Fraction(1,3),0,Fraction(1,5),0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,0,0,0,0,0,0,0,0],
    [0,Fraction(1,5),0,Fraction(1,3),0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,0,0,0,0,0,0,0],
    [0,0,Fraction(1,5),0,0,0,Fraction(1,8),Fraction(1,5),0,0,0,0,0,0,0,0],
    [Fraction(1,3),Fraction(1,5),0,0,0,Fraction(1,8),0,0,Fraction(1,5),Fraction(1,8),0,0,0,0,0,0],
    [Fraction(1,3),Fraction(1,5),Fraction(1,5),0,Fraction(1,5),0,Fraction(1,8),0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,0,0,0,0],
    [0,Fraction(1,5),Fraction(1,5),Fraction(1,3),0,Fraction(1,8),0,Fraction(1,5),0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,0,0,0],
    [0,0,Fraction(1,5),Fraction(1,3),0,0,Fraction(1,8),0,0,0,Fraction(1,8),Fraction(1,5),0,0,0,0],
    [0,0,0,0,Fraction(1,5),Fraction(1,8),0,0,0,Fraction(1,8),0,0,Fraction(1,3),Fraction(1,5),0,0],
    [0,0,0,0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,Fraction(1,5),0,Fraction(1,8),0,Fraction(1,3),Fraction(1,5),Fraction(1,5),0],
    [0,0,0,0,0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,Fraction(1,8),0,Fraction(1,5),0,Fraction(1,5),Fraction(1,5),Fraction(1,3)],
    [0,0,0,0,0,0,Fraction(1,8),Fraction(1,5),0,0,Fraction(1,8),0,0,0,Fraction(1,5),Fraction(1,3)],
    [0,0,0,0,0,0,0,0,Fraction(1,5),Fraction(1,8),0,0,0,Fraction(1,5),0,0],
    [0,0,0,0,0,0,0,0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,Fraction(1,3),0,Fraction(1,5),0],
    [0,0,0,0,0,0,0,0,0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,Fraction(1,5),0,Fraction(1,3)],
    [0,0,0,0,0,0,0,0,0,0,Fraction(1,8),Fraction(1,5),0,0,Fraction(1,5),0]
    ])
    return latex(M)


def output(keyinput):
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/chess.html'>"
