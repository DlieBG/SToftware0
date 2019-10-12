from sympy import *
from functions import root
from functions import derivative
from functions import extrems
from functions import turns
from functions import integral


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
