from sympy import *
from fractions import Fraction

def hook(keyinput):
    #Keywords definieren
    if "schach" in keyinput:
        if "anfang" in keyinput or "uebergang" in keyinput:
            return anfangsmatrix()
        if "stationaer" in keyinput:
            return stationaereverteilung()
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
    return "Übergangsmatrix:$$"+latex(M)+"$$"
def stationaereverteilung():
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
    V = Matrix([
        [1],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
    ])
    return "Stationäre Verteilung:$$"+latex(N(M**100*V, 10))+"$$"

def output(keyinput):
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/chess.html'>"
