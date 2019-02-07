from sympy import *

def hook(keyinput):
    if "x" in keyinput or "f(x)" in keyinput:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""
    
    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part:
            term = part
            if "=" in term:
                term = term.split("=")[1]
            term = term.replace("y=", "")
            term = term.replace("f(x)=", "")

    if term is not "":
        return output(term)
    else:
        return("")

def output(out):
    print("")
    return "\n<iframe src='http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/plot/index.html?"+out+"' />"
