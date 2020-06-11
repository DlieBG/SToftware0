from sympy.parsing.sympy_parser import parse_expr
from functionallity import *


def isTerm(possibleTerm):
    if "=" not in possibleTerm:
        return isPars(possibleTerm)
    l=possibleTerm.split("=")[0]
    r = possibleTerm.split("=")[1]
    return isPars(l) and isPars(r)


def isPars(possibleTerm):
    try:
        parse_expr(possibleTerm)
    except:
        return False
    finally:
        return True


def isfloat(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


def clean(s):#mathematical clean
    s = s.lower()
    s = s.replace("^", "**")
    s = s.replace("f(x)=", "")
    s = s.replace("y=", "")
    return s
