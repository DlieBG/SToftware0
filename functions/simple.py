from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def hook(keyinput):
    if ("x" in keyinput or "*" in keyinput or "+" in keyinput or "/" in keyinput or "-" in keyinput) and "exit" not in keyinput.lower() and keyinput is not "":
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    if "=" not in keyinput:
        term = ""
        
        parts = keyinput.split(' ')
        for part in parts:
            if "*" in part or "+" in part or "/" in part or "-" in part or part is "x":
                term = part
                if "=" in term:
                    term = term.split("=")[1]
                term = term.replace("y=", "")
                term = term.replace("f(x)=", "")

        if term is not "":
            return simple(term)
        else:
            return("Ihre Eingabe konnte nicht richtig erkannt werden!")
    else:
        term = ""
        left = ""
        right = ""
    
        parts = keyinput.split(' ')
        for part in parts:
            if "=" in part:
                term = part
                left = part.split("=")[0]
                right = part.split("=")[1]
    
        if term is not "" and left is not "" and right is not "":
            return simpleEq(left,right)
        else:
            print("Fehler")
            return "Fehler"
        
def simple(term):
    out = sympify(parse_expr(term))
    return output(out)
    
def simpleEq(left,right):
    left = sympify(parse_expr(left))
    right = sympify(parse_expr(right))
    return output2(left,right)

def output(out):
    print("\n"+str(out))
    return "\nEingabe: $$"+str(latex(out))+"$$"
    
def output2(left,right):
    print("\n"+str(left)+"="+str(right))
    return "\nEingabe: $$"+str(latex(left))+"="+str(latex(right))+"$$"
