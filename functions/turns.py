from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def hook():
    return ["wendestelle", "wendepunkt", "wende", "turn"]


def getComponents(term):
    return turns(term)


def turns(term):
    x = symbols('x')
    init_printing()
    deriv = diff(term, x, 2)
    turns = solve(deriv, x)
    turnsy=[]
    for turn in turns:
        turnsy.append(parse_expr(term).subs(x,turn))
    deriv2 = diff(term, x, 3)
    deriv2y=[]
    for turn in turns:
        deriv2y.append(deriv2.subs(x,turn))
    return output(turns, turnsy, deriv2y)


def output(turns, turnsy, deriv2y):
    texout="\nMögliche Wendestellen: $$x="+str(latex(turns))+"$$"
    print("\nMögliche Wendestellen sind: \nx="+str(turns))
    for turn in turns:
        print("\nf("+str(turn)+")= "+str(turnsy[turns.index(turn)]))
        print("\nf'''("+str(turn)+")= "+str(deriv2y[turns.index(turn)]))
        texout+="\n$$f("+str(latex(turn))+")= "+str(latex(turnsy[turns.index(turn)]))+"$$"
        texout+="\n$$f'''("+str(latex(turn))+")= "+str(latex(deriv2y[turns.index(turn)]))+"$$"
    return texout
