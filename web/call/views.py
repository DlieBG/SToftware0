from django.http import HttpResponse

from SToftware0.functions import derivative

def index(request):
    return HttpResponse(derivative.hook("ableitung x**2"))