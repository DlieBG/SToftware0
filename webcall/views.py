from django.http import HttpResponse

from functions import derivative

def index(request):
    webinput = request.GET.get("q", "")
    html = '<script type="text/javascript" async \nsrc="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>'
    
    html += derivative.hook(webinput)

    return HttpResponse(html)