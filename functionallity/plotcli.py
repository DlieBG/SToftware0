from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def hook():
    return ["plot", "zeichne"]

def needsterm():
    return True

def getComponents(term, parts):

    a = ""
    b = ""

    for part in parts:
        if isfloat(part) and a is "":
            a = part
        elif isfloat(part) and a is not "" and b is "":
            b = part

    if term is not "":
        return cligraph(term, a, b)
    else:
        print("Es konnte kein Term gefunden werden")
        return ""


def isfloat(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


def cligraph(term, a, b):
    x = symbols('x')
    init_printing(use_unicode=True)
    term=parse_expr(term)
    
    if a is not "":
        a=float(a)
       
    if b is not "":
        b=float(b)
        
    if a is "" and b is "":
        a=-10
        b=10
    if a is "":
        a=b-20
    if b is "":#just in case
        b=a+20
    ymax=Max(term.subs(x,a),term.subs(x,b))
    ymin=Min(term.subs(x,a),term.subs(x,b))
    
    #max min
    deriv = diff(term, x, 1)
    extremes = solve(deriv, x)
    for extrem in extremes:
        ymax=Max(ymax,term.subs(x,extrem))
        ymin=Min(ymin,term.subs(x,extrem))
    
    return output(term,a,b,ymin,ymax,deriv)
    
    
def output(term,a,b,ymin,ymax,deriv):
    x = symbols('x')
    init_printing(use_unicode=True)
    xvals=[]
    for n in range(11):
        xvals.append(a+(b-a)/10*n)#range-1=>10
        
    yvals=[]
    for n in range(11):
        yvals.append(ymin+(ymax-ymin)/10*n)
        
    marks=[]
    clisymbols=[]
    for xcoord in xvals:
        y=term.subs(x,xcoord)
        derivy=deriv.subs(x,xcoord)
        d=0
        for i in range(len(yvals)):
            if abs(yvals[i]-y)<abs(yvals[d]-y):#what is nearest value
                d=i
        marks.append(d)
        if derivy==0:
            clisymbols.append("-")
        elif Min(derivy,0)==derivy:
            clisymbols.append("\\")
        elif Max(derivy,0)==derivy:
            clisymbols.append("/")
    arr=[]
    for arrx in range(len(marks)):
        arr.append([])
        for arry in range(11):
            arry=10-arry
            if marks[arrx]==arry:
                #arr[arrx].append("-")
                arr[arrx].append(clisymbols[arrx])
            else:
                arr[arrx].append(" ")
    print("")
    for arry in range(11):
        out=""
        for arrx in range(11):
            out+=str(arr[arrx][arry])
        out+=" |~"+str(yvals[10-arry])
        print(out)
    print("von "+str(xvals[0])+" bis "+str(xvals[-1]))
