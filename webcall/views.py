from django.http import HttpResponse

from functions import eastereggs
from functions import derivative
from functions import integral
from functions import root
from functions import solve

def index(request):
    webinput = request.GET.get("q", "")
    html = '<script type="text/javascript" async \nsrc="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>'
    
    html += eastereggs.hook(webinput)
    html += derivative.hook(webinput)
    html += integral.hook(webinput)
    html += root.hook(webinput)
    html += solve.hook(webinput)

    return HttpResponse(html)