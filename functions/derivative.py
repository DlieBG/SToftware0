from sympy import *

def derivative(term, height):
    x = symbols('x')
    init_printing(use_unicode=True)
    return diff(term, x, height)