from sympy import *

def hook(keyinput):
    if "wendestelle" in keyinput.lower() or "wendepunkt" in keyinput.lower() or "wende" in keyinput.lower() or "turn" in keyinput.lower():
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
        return turns(term)
    else:
        print("Fehler")
        return "Fehler"
        
def turns(term):
    x = symbols('x')
    init_printing(use_unicode=True)
    deriv = diff(term, x, 2)
    turns = solve(deriv, x)
    turnsy=[]
    for turn in turns:
        turnsy.append(term.subs(x,turn))
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
        #texout+="\n$$f'''("+str(latex(turn))+")= "+str(latex(deriv2y[turns.index(turn)]))+"$$"
    return texout
