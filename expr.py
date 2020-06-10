from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from functionallity import *

keywords=[]


def readinKeywords(keys):
    for key in keys:
        keywords.append(key)

def outall():
    print(str(keywords))


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


def findTerm(keyinput):
    parts = keyinput.split(' ')
    for part in parts:
        if isTerm(part) and not isKeyword(part):
            return part

    return ""


def isKeyword(s):
    return s in keywords


def isfloat(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


def clean(s):
    s = s.lower()
    s = s.replace("^", "**")
    s = s.replace("f(x)=", "")
    s = s.replace("y=", "")
    return s


def splitKandTandP(s):
    parts=[]
    keyword=""
    term = ""
    splitted=s.split(" ")
    for part in splitted:
        if not isKeyword(part):
            if isTerm(part):
                if not isfloat(part) and term is "":
                    term=part
                elif not isfloat(part) and "x" not in term and "x" in part:
                    parts.append(term)
                    term = part
            parts.append(part)
        elif keyword is "":
            keyword=part
    return keyword, term, parts
