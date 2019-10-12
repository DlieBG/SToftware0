from functions import eastereggs
from functions import derivative
from functions import integral
from functions import root
from functions import solve
from functions import extrems
from functions import simple
from functions import discussion
from functions import turns
from functions import plotcli
from functions import kamel
from functions import feedback
from functions import polynomial
from functions import weather
from functions import binomial
from functions import chessproblem
from functions import fcm

from expr import *

print("Willkommen bei SToftware0 by bschwering & ftuente\n\nBesuche doch mal die Website benedikt-schwering.de/SToftware0\n")


def main():
    readin()
    outall()
    keyinput=""
    while "exit" not in keyinput:
        print("\n\nBitte gib eine Aufgabe ein! (Bsp.: 1. Ableitung von x**2)")
        keyinput = input()
        keyinput=clean(keyinput)
        key, term, parts = splitKandTandP(keyinput)
        print("key: "+str(key)+"\nterm: "+str(term)+"\n"+str(parts))
        fcm.getComponents(keyinput)

        if term is not "":
            simple.getComponents(term)

        eastereggs.getComponents(keyinput)

        if key is not "":
            if term is not "":
                if key in discussion.hook():
                    discussion.getComponents(term)

                if key in root.hook():
                    root.getComponents(term)

                if key in extrems.hook():
                    extrems.getComponents(term)

                if key in turns.hook():
                    extrems.getComponents(term)


                if key in derivative.hook() and parts is not []:
                    derivative.getComponents(term, parts)

                if key in integral.hook() and parts is not []:
                    integral.getComponents(term, parts)


                if key in solve.hook() and "=" in term:
                    solve.getComponents(term)


                if key in plotcli.hook() and parts is not []:
                    plotcli.getComponents(term, parts)

                if key in polynomial.hook() and "=" in term:
                    polynomial.getComponents(term)

            if key in binomial.hook() and parts is not []:
                binomial.getComponents(parts)

            if key in chessproblem.hook() and parts is not []:
                chessproblem.getComponents(parts)


            # not on cmd line
            if key in kamel.hook():
                kamel.getComponents()

            if key in feedback.hook():
                feedback.getComponents()

            if key in weather.hook():
                weather.getComponents(parts)





def readin():
    readinKeywords(fcm.hook())
    readinKeywords(simple.hook())
    readinKeywords(discussion.hook())
    readinKeywords(eastereggs.hook())
    readinKeywords(derivative.hook())
    readinKeywords(integral.hook())
    readinKeywords(root.hook())
    readinKeywords(extrems.hook())
    readinKeywords(turns.hook())
    readinKeywords(solve.hook())
    readinKeywords(plotcli.hook())
    readinKeywords(kamel.hook())
    readinKeywords(feedback.hook())
    readinKeywords(polynomial.hook())
    readinKeywords(weather.hook())
    readinKeywords(binomial.hook())
    readinKeywords(chessproblem.hook())



main()