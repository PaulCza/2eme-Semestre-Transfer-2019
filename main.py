#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## main.py
## File description:
## blabla
##

import math
import sys
import string

def horner(poly, n, x): 
    result = poly[0]
    for i in range(1, n):
        result = result*x + poly[i]
    return result

def make_expression(yolo):
    number_string = yolo.split('*')
    try:
        number_string = [int(i) for i in number_string]
    except ValueError:
        sys.exit(84)
    P = number_string[::-1]
    return P


def make_greater_list(count, argv, x):
    a = 0
    result = 1
    while (a < count):
        r1 = make_expression(argv[a])
        r2 = make_expression(argv[a + 1])
        if (r2 == 0):
            exit(84)
        r3 = horner(r1, len(r1), x) / horner(r2, len(r2), x)
        result = result * r3
        a = a + 2
    return result
    
def main(argv):
    if (len(sys.argv) == 1):
        exit(84)
    count = (len(sys.argv) - 1)
    if (count % 2 == 0):
        x = 0
        while (x < 1.001):
            result = make_greater_list(count, argv, x)
            print("%.3f" % x, end='')
            print(" -> ", end='')
            print("%.5f" % result)
            x = x + 0.001
    else:
        exit(84)