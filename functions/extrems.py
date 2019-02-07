from sympy import *

def hook(keyinput):
    if "extremstellen" in keyinput.lower() or "extrempunkte" in keyinput.lower() or "maxima" in keyinput.lower() or "minima" in keyinput.lower():
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    term = ""

    parts = keyinput.split(' ')
    for part in parts:
        if "x" in part and "maxima" not in part:
            term = part
            if "=" in term:
                term = term.split("=")[1]
    
    if term is not "":
        return extrems(term)
    else:
        print("Fehler")
        return "Fehler"
        
def extrems(term):
    x = symbols('x')
    init_printing(use_unicode=True)
    deriv = diff(term, x, 1)
    extremes = solve(deriv, x)
    extremsy=[]
    for extrem in extremes:
        extremsy.append(term.subs(x,extrem))
    deriv2 = diff(term, x, 2)
    deriv2y=[]
    for extrem in extremes:
        deriv2y.append(deriv2.subs(x,extrem))
    return output(extremes, extremsy, deriv2y)

def output(extremes, extremsy, deriv2y):
    texout="\nMögliche Extremstellen: $$x="+str(latex(extremes))+"$$"
    print("\nMögliche Extremstellen sind: \nx="+str(extremes))
    for extrem in extremes:
        print("\nf("+str(extrem)+")= "+str(extremsy[extremes.index(extrem)]))
        print("\nf''("+str(extrem)+")= "+str(deriv2y[extremes.index(extrem)]))
        texout+="\n$$f("+str(latex(extrem))+")= "+str(latex(extremsy[extremes.index(extrem)]))+"$$"
        #texout+="\n$$f''("+str(latex(extrem))+")= "+str(latex(deriv2y[extremes.index(extrem)]))+"$$"
    return texout
