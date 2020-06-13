def hook():
    return ["plot"]


def needsterm():
    return True


def getComponents(term, parts):
    return output(term)


def output(out):
    print("")
    return "\n<iframe frameborder='0' scrolling='no' style='width: 98vw; height: 350px' src='https://benedikt-schwering.de//SToftware0/html/mobile/functions/plot/index.html?"+out+"'></iframe><br>"
