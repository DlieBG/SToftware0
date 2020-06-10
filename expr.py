from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def isTerm(possibleTerm):
    try:
        parse_expr(possibleTerm)
    except:
        return False
    finally:
        return True

def findTerm(keyinput):
    parts = keyinput.split(' ')
    for part in parts:
        if isTerm(part) and not isKeyword(part):
            return part

    return ""
