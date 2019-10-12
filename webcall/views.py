from django.http import HttpResponse

from functions import eastereggs
from functions import derivative
from functions import integral
from functions import root
from functions import solve
from functions import extrems
from functions import simple
from functions import discussion
from functions import turns
from functions import plot
from functions import kamel
from functions import feedback
from functions import polynomial
from functions import weather
from functions import binomial
from functions import chessproblem
from functions import fcm
from expr import *


def index(request):
    keyinput = request.POST.get("ST0q", "")

    html = '<script type="text/javascript" async \nsrc="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>'
    try:
        keyinput = clean(keyinput)
        key, term, parts = splitKandTandP(keyinput)
        print("key: " + str(key) + "\nterm: " + str(term) + "\n" + str(parts))
        html += fcm.getComponents(keyinput)
        if "x" in term:
            html += plot.getComponents(term)
        if term is not "":
            html += simple.getComponents(term)

        html += eastereggs.getComponents(keyinput)

        if key is not "":
            if term is not "":
                if key in discussion.hook():
                    html += discussion.getComponents(term)

                if key in root.hook():
                    html += root.getComponents(term)

                if key in extrems.hook():
                    html += extrems.getComponents(term)

                if key in turns.hook():
                    html += extrems.getComponents(term)

                if key in derivative.hook() and parts is not []:
                    html += derivative.getComponents(term, parts)

                if key in integral.hook() and parts is not []:
                    html += integral.getComponents(term, parts)

                if key in solve.hook() and "=" in term:
                    html += solve.getComponents(term)


                if key in polynomial.hook() and "=" in term:
                    html += polynomial.getComponents(term)

            if key in binomial.hook() and parts is not []:
                html += binomial.getComponents(parts)

            if key in chessproblem.hook() and parts is not []:
                html += chessproblem.getComponents(parts)

            # not on cmd line
            if key in kamel.hook():
                html += kamel.getComponents()

            if key in feedback.hook():
                html += feedback.getComponents()

            if key in weather.hook():
                html += weather.getComponents(parts)
    except:
        html +="<h1>FEHLER</h1> Entweder <h2>DU bist schuld</h2> oder das Programm ist schuld"
    finally:
        return HttpResponse(html)
