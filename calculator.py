# https://github.com/sukiliuuu/lab11-SL-RWW/
# My partner never repled to my attempts at communication so I completed the parts I could
# Partner 1: Suki Liu
# Partner 2: Ramey Webb Webb
import math
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)
def exponent(a, b):
    return a ** b
