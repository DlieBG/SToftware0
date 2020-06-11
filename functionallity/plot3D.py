def hook():
    return []

def needsterm():
    return True

def getComponents(term,parts):
    return output(term)


def output(out):
    print("")
    return "\n<iframe frameborder='0' scrolling='no' style='width: 98vw; height: 350px' src='http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/plot3D/index.html?"+out+"'></iframe><br>"
