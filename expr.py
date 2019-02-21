from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def isTerm(term):
    try:
        parse_expr(term)
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
    
def isKeyword(s):
    keywords=["ableit","derivate"]#TODO add all options (if included)
    for phrase in keywords:
        if phrase in s:
            return True
    return False
