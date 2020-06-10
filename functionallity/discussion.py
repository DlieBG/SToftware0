from sympy import *
from functionallity import root
from functionallity import derivative
from functionallity import extrems
from functionallity import turns
from functionallity import integral


def hook():
    return ["kurvendiskussion", "diskussion", "diskutiere", "discuss"]


def getComponents(term):
    return output(term)


def output(term):
    html = root.getComponents(term)
    html += derivative.getComponents(term, [" 1."])
    html += derivative.getComponents(term, [" 2."])
    html += extrems.getComponents(term)
    html += turns.getComponents(term)

    return html
