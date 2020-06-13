from functionallity import derivative, extrems, integral, root, turns


def hook():
    return ["kurvendiskussion", "diskussion", "diskutiere", "discuss"]


def needsterm():
    return True


def getComponents(term, parts):
    return output(term)


def output(term):
    html = root.getComponents(term, list())
    html += derivative.getComponents(term, [" 1."])
    html += derivative.getComponents(term, [" 2."])
    html += extrems.getComponents(term, list())
    html += turns.getComponents(term, list())

    return html
