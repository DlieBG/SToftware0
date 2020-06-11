from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def hook():
    return ["extremstellen", "extrempunkte", "maxima", "minima"]

def needsterm():
    return True

def getComponents(term,parts):
    return extrems(term)


def extrems(term):
    x = symbols('x')
    init_printing()
    deriv = diff(term, x, 1)
    extremes = solve(deriv, x)
    extremsy=[]
    for extrem in extremes:
        extremsy.append(parse_expr(term).subs(x,extrem))
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
        texout += "\n$$f("+str(latex(extrem))+")= "+str(latex(extremsy[extremes.index(extrem)]))+"$$"
        texout += "\n$$f''("+str(latex(extrem))+")= "+str(latex(deriv2y[extremes.index(extrem)]))+"$$"
    return texout
