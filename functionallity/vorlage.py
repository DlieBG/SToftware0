from sympy import *  # not necessary, but mostly needed


def hook(keyinput):
    # return the keywords this module should react to
    return ["keyword 1", "keyword2"]


def needsterm():  # return if term is needed in getComponents
    return True


def getComponents(term, parts):

    # processing

    return functionX(term, whatever := None)


def functionX(term, whatever):
    # whatever this module is made for
    return output(out := None, term)


def output(out, term):
    # output to cli and return to html
    print("asdf")
    return "asdf"
