def hook():
    return []


def getComponents(term):
    return output(term)


def output(out):
    print("")
    return "\n<iframe frameborder='0' scrolling='no' style='width: 98vw; height: 350px' src='http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/plot/index.html?"+out+"'></iframe><br>"
