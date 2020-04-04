from sympy import *

def hook(keyinput):
    if "polinom" not in keyinput and ("x" in keyinput or "*" in keyinput or "+" in keyinput or "/" in keyinput or "-" in keyinput or len(keyinput.split(" ")) is 1) and "exit" not in keyinput and "=" not in keyinput and keyinput is not "":
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""
    
    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part:
            term = part

    if term is not "":
        return output(term)
    else:
        return("")

def output(out):
    print("")
    return "\n<iframe frameborder='0' scrolling='no' style='width: 98vw; height: 350px' src='https://benedikt-schwering.de/SToftware0/html/mobile/functions/plot/index.html?"+out+"'></iframe><br>"
