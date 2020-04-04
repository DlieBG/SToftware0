from sympy import *
from fractions import Fraction
init_printing(use_unicode=True)

def hook(keyinput):
    #Keywords definieren
    if "schach" in keyinput:
        if "king" in keyinput or "koenig" in keyinput:
            return king()
        if "queen" in keyinput or "dame" in keyinput:
            return queen()
        if "tower" in keyinput or "turm" in keyinput:
            return tower()
        if "walker" in keyinput or "lauefer" in keyinput:
            return walker()
        if "jumper" in keyinput or "springer" in keyinput:
            return jumper()
    return ""
    
V = Matrix([
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
    [1],
])
I=eye(16,16)

def king():
    MK = Matrix([
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
    
    MK2 = Matrix([
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
    #[0,0,0,0,0,0,0,0,0,0,Fraction(1,8),Fraction(1,5),0,0,Fraction(1,5),0]
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    ])
    MK2=MK2-I
    E=linsolve((MK2,V),(symbols('a')))
    return "Matrix: $$"+latex(MK)+"$$ Stationaere Verteilung: $$"+latex(E)+"$$"
    
def queen():
    MQ = Matrix(
    [
    [0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),0,0,Fraction(1,9)],
    [Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),0,0],
    [Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),0,Fraction(1,11),0,0,0,Fraction(1,9),0],
    [Fraction(1,9),Fraction(1,9),Fraction(1,9),0,0,0,Fraction(1,11),Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),Fraction(1,9),0,0,Fraction(1,9)],
    [Fraction(1,9),Fraction(1,9),0,0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,9),0],
    [Fraction(1,9),Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,9)],
    [0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0],
    [0,0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,0,Fraction(1,11),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,9)],
    [Fraction(1,9),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,11),0,0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),0,0],
    [0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),0],
    [Fraction(1,9),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,9)],
    [0,Fraction(1,9),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,0,Fraction(1,9),Fraction(1,9)],
    [Fraction(1,9),0,0,Fraction(1,9),Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),Fraction(1,11),0,0,0,Fraction(1,9),Fraction(1,9),Fraction(1,9)],
    [0,Fraction(1,9),0,0,0,Fraction(1,11),0,Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9)],
    [0,0,Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),0,Fraction(1,9)],
    [Fraction(1,9),0,0,Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),0]
    ]
    )
    
    MQ2 = Matrix(
    [
    [0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),0,0,Fraction(1,9)],
    [Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),0,0],
    [Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),0,Fraction(1,11),0,0,0,Fraction(1,9),0],
    [Fraction(1,9),Fraction(1,9),Fraction(1,9),0,0,0,Fraction(1,11),Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),Fraction(1,9),0,0,Fraction(1,9)],
    [Fraction(1,9),Fraction(1,9),0,0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,9),0],
    [Fraction(1,9),Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,9)],
    [0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0],
    [0,0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,0,Fraction(1,11),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,9)],
    [Fraction(1,9),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,11),0,0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),0,0],
    [0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),0],
    [Fraction(1,9),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,9)],
    [0,Fraction(1,9),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,0,Fraction(1,9),Fraction(1,9)],
    [Fraction(1,9),0,0,Fraction(1,9),Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),Fraction(1,11),0,0,0,Fraction(1,9),Fraction(1,9),Fraction(1,9)],
    [0,Fraction(1,9),0,0,0,Fraction(1,11),0,Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9)],
    [0,0,Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),0,Fraction(1,9)],
    #[Fraction(1,9),0,0,Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),0]
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    ]
    )
    MQ2=MQ2-I
    E=linsolve((MQ2,V),(symbols('a')))
    return "Matrix: $$"+latex(MQ)+"$$ Stationaere Verteilung: $$"+latex(E)+"$$"
    
def tower():
    MT = Matrix(
    [
    [0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0],
    [Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0],
    [Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0],
    [Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6)],
    [Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,Fraction(1,6),0,0,0],
    [0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,0,Fraction(1,6),0,0],
    [0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0,0,0,Fraction(1,6),0],
    [0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6),0,0,0,Fraction(1,6)],
    [Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0],
    [0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0],
    [0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0],
    [0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6)],
    [Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6)],
    [0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6)],
    [0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6)],
    [0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0]
    ]
    )
    
    MT2 = Matrix(
    [
    [0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0],
    [Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0],
    [Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0],
    [Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6)],
    [Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,Fraction(1,6),0,0,0],
    [0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,0,Fraction(1,6),0,0],
    [0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0,0,0,Fraction(1,6),0],
    [0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6),0,0,0,Fraction(1,6)],
    [Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0],
    [0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0],
    [0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0],
    [0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6)],
    [Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6)],
    [0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6)],
    [0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6)],
    #[0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0]
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    ]
    )
    MT2=MT2-I
    E=linsolve((MT2,V),(symbols('a')))
    return "Matrix: $$"+latex(MT)+"$$ Stationaere Verteilung: $$"+latex(E)+"$$"
    
def walker():
    MW = Matrix([
    [0,0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,3)],
    [0,0,0,0,Fraction(1,3),0,Fraction(1,5),0,0,0,0,Fraction(1,3),0,0,0,0],
    [0,0,0,0,0,Fraction(1,5),0,Fraction(1,3),Fraction(1,3),0,0,0,0,0,0,0],
    [0,0,0,0,0,0,Fraction(1,5),0,0,Fraction(1,5),0,0,Fraction(1,3),0,0,0],
    [0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,3),0],
    [Fraction(1,3),0,Fraction(1,3),0,0,0,0,0,Fraction(1,3),0,Fraction(1,5),0,0,0,0,Fraction(1,3)],
    [0,Fraction(1,3),0,Fraction(1,3),0,0,0,0,0,Fraction(1,5),0,Fraction(1,3),Fraction(1,3),0,0,0],
    [0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,5),0,0,Fraction(1,3),0,0],
    [0,0,Fraction(1,3),0,0,Fraction(1,5),0,0,0,0,0,0,0,Fraction(1,3),0,0],
    [0,0,0,Fraction(1,3),Fraction(1,3),0,Fraction(1,5),0,0,0,0,0,Fraction(1,3),0,Fraction(1,3),0],
    [Fraction(1,3),0,0,0,0,Fraction(1,5),0,Fraction(1,3),0,0,0,0,0,Fraction(1,3),0,Fraction(1,3)],
    [0,Fraction(1,3),0,0,0,0,Fraction(1,5),0,0,0,0,0,0,0,Fraction(1,3),0],
    [0,0,0,Fraction(1,3),0,0,Fraction(1,5),0,0,Fraction(1,5),0,0,0,0,0,0],
    [0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,3),0,Fraction(1,5),0,0,0,0,0],
    [0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,5),0,Fraction(1,3),0,0,0,0],
    [Fraction(1,3),0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,5),0,0,0,0,0]
    ])
    return "Matrix: $$"+latex(MW)+"$$"
    
def jumper():
    MJ = Matrix([
    [0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,4),0,0,0,0,0,0],
    [0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,3),0,Fraction(1,4),0,0,0,0,0],
    [0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,4),0,Fraction(1,3),0,0,0,0],
    [0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,4),0,0,0,0,0],
    [0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,3),0,0],
    [0,0,0,Fraction(1,2),0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,2),0,Fraction(1,3),0],
    [Fraction(1,2),0,0,0,0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,3),0,Fraction(1,2)],
    [0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,3),0],
    [0,Fraction(1,3),0,0,0,0,Fraction(1,4),0,0,0,0,0,0,0,Fraction(1,3),0],
    [Fraction(1,2),0,Fraction(1,3),0,0,0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,2)],
    [0,Fraction(1,3),0,Fraction(1,2),Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,2),0,0,0],
    [0,0,Fraction(1,3),0,0,Fraction(1,4),0,0,0,0,0,0,0,Fraction(1,3),0,0],
    [0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,4),0,0,0,0,0],
    [0,0,0,0,Fraction(1,3),0,Fraction(1,4),0,0,0,0,Fraction(1,3),0,0,0,0],
    [0,0,0,0,0,Fraction(1,4),0,Fraction(1,3),Fraction(1,3),0,0,0,0,0,0,0],
    [0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,4),0,0,0,0,0,0]
    ])
    
    MJ2 = Matrix([
    [0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,4),0,0,0,0,0,0],
    [0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,3),0,Fraction(1,4),0,0,0,0,0],
    [0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,4),0,Fraction(1,3),0,0,0,0],
    [0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,4),0,0,0,0,0],
    [0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,3),0,0],
    [0,0,0,Fraction(1,2),0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,2),0,Fraction(1,3),0],
    [Fraction(1,2),0,0,0,0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,3),0,Fraction(1,2)],
    [0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,3),0],
    [0,Fraction(1,3),0,0,0,0,Fraction(1,4),0,0,0,0,0,0,0,Fraction(1,3),0],
    [Fraction(1,2),0,Fraction(1,3),0,0,0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,2)],
    [0,Fraction(1,3),0,Fraction(1,2),Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,2),0,0,0],
    [0,0,Fraction(1,3),0,0,Fraction(1,4),0,0,0,0,0,0,0,Fraction(1,3),0,0],
    [0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,4),0,0,0,0,0],
    [0,0,0,0,Fraction(1,3),0,Fraction(1,4),0,0,0,0,Fraction(1,3),0,0,0,0],
    [0,0,0,0,0,Fraction(1,4),0,Fraction(1,3),Fraction(1,3),0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,4),0,0,0,0,0,0]
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    ])
    MJ2=MJ2-I
    E=linsolve((MJ2,V),(symbols('a')))
    return "Matrix: $$"+latex(MJ)+"$$ Stationaere Verteilung: $$"+latex(E)+"$$"
