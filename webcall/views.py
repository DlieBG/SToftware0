from django.http import HttpResponse

from functions import eastereggs
from functions import derivative
from functions import integral
from functions import root
from functions import solve
from functions import extrems
from functions import simple

def index(request):
    webinput = request.POST.get("ST0q", "")
    html = '<script type="text/javascript" async \nsrc="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>'
    
    html += eastereggs.hook(webinput)
    html += derivative.hook(webinput)
    html += integral.hook(webinput)
    html += root.hook(webinput)
    html += solve.hook(webinput)
    html += extrems.hook(webinput)
    html += simple.hook(webinput)

    return HttpResponse(html)
