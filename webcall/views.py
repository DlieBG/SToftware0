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
from functions import dromedar
from functions import feedback
from functions import polynomial
from functions import weather
from functions import binomial
from functions import chessproblem
from functions import fcm

def index(request):
    webinput = request.POST.get("ST0q", "")
    webinput = webinput.lower()
    webinput = webinput.replace("^", "**")
    webinput = webinput.replace("f(x)=", "")
    webinput = webinput.replace("y=", "")
    html = '<script type="text/javascript" async \nsrc="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>'
    try:
        html += fcm.hook(webinput)
        html += simple.hook(webinput)
        html += plot.hook(webinput)
        html += discussion.hook(webinput)
        html += eastereggs.hook(webinput)
        html += derivative.hook(webinput)
        html += integral.hook(webinput)
        html += root.hook(webinput)
        html += extrems.hook(webinput)
        html += turns.hook(webinput)
        html += solve.hook(webinput)
        html += kamel.hook(webinput)
        html += dromedar.hook(webinput)
        html += feedback.hook(webinput)
        html += polynomial.hook(webinput)
        html += weather.hook(webinput)
        html += binomial.hook(webinput)
        html += chessproblem.hook(webinput)
    except:
        html +="<h1>FEHLER</h1> Entweder <h2>DU bist schuld</h2> oder das Programm ist schuld"
    finally:
        return HttpResponse(html)
