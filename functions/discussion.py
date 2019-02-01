from sympy import *
from functions import root
from functions import derivative
from functions import extrems
from functions import turns
from functions import integral

def hook(keyinput):
    #Keywords definieren
    if "kurvendiskussion" in keyinput.lower() or "diskussion" in keyinput.lower() or "diskutiere" in keyinput.lower() or "discuss" in keyinput.lower():
        return output(keyinput)
    return ""

def output(keyinput):
    html = root.getComponents(keyinput)
    html += derivative.getComponents(keyinput+" 1.")
    html += derivative.getComponents(keyinput+" 2.")
    html += extrems.getComponents(keyinput)
    html += turns.getComponents(keyinput)
    html += integral.getComponents(keyinput)
    
    return html