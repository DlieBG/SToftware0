from sympy import *
from functionallity import root
from functionallity import derivative
from functionallity import extrems
from functionallity import turns
from functionallity import integral


def hook():
    return ["kurvendiskussion", "diskussion", "diskutiere", "discuss"]

def needsterm():
    return True

def getComponents(term,parts):
    return output(term)


def output(term):
    html = root.getComponents(term,list())
    html += derivative.getComponents(term, [" 1."])
    html += derivative.getComponents(term, [" 2."])
    html += extrems.getComponents(term,list())
    html += turns.getComponents(term,list())

    return html
