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

def index(request):
    webinput = request.POST.get("ST0q", "")
    webinput = webinput.replace("^", "**")
    html = '<script type="text/javascript" async \nsrc="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>'
    
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

    return HttpResponse(html)