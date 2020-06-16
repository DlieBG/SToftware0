from django.http import HttpResponse

import regex
import functionallity as funct
from functionallity import *
from expr import *

def process(inp):
    inp = clean(inp)
    inp = inp.strip()
    inp = regex.split(r"\s+", inp, flags=regex.UNICODE)
    modu = "simple"
    if len(inp) == 0:
        return ""
    elif len(inp) == 1:
        for module in funct.__allweb__:
            if inp[0] in getattr(funct, module).hook():
                if not getattr(funct, module).needsterm():
                    return getattr(funct, modu).getComponents(list())
        if isTerm(inp[0]):
            return funct.simple.getComponents(inp[0],list())
    else:
        for module in funct.__allweb__:
            if inp[0] in getattr(funct, module).hook():
                modu = module
                break
        if getattr(funct, modu).needsterm():
            term = None  # find term
            termi = None
            for i in range(1, len(inp)):
                if isTerm(inp[i]):
                    if not term:
                        term = inp[i]
                        termi = i
                    # maybe first parseble argument is term always
                    elif "x" in inp[i] and "x" not in term:
                        term = inp[i]
                        termi = i
            if not term:
                return "<h1>No Term found</h1>"
            else:
                parts = list()
                for i in range(1, len(inp)):
                    if i != termi:
                        parts.append(inp[i])
                return getattr(funct, modu).getComponents(term, parts)

        else:
            parts = inp[1::]
            return getattr(funct, modu).getComponents(parts)

    inp = " ".join(inp)
    return funct.eastereggs.getComponents(inp)


def index(request):
    keyinput = request.POST.get("ST0q", "")

    html = '<script type="text/javascript" async \nsrc="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>'
    #try:
    html+=process(keyinput)
    #except:
        #html +="<h1>FEHLER</h1> Entweder <h2>DU bist schuld</h2> oder das Programm ist schuld"
    #finally:
    return HttpResponse(html)
