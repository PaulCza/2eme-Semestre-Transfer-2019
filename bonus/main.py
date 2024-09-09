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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def horner(poly, n, x): 
    result = poly[0]
    for i in range(1, n):
        result = result*x + poly[i]
    return result

def make_expression(yolo):
    number_string = yolo.split('*')
    number_string = [int(i) for i in number_string]
    P = number_string[::-1]
    return P


def check(yolo):
    a = len(yolo) - 1
    b = 0
    while (b < a):
        try:
            val = float(yolo[b])
        except ValueError:
            sys.exit(84)
        b = b + 2

def main(argv):
    px = []
    py = []
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    if (len(sys.argv) == 3):
        check(argv[0])
        check(argv[1])
        poly = make_expression(argv[0])
        poly2 = make_expression(argv[1])
        x = 0
        r1 = round(horner(poly, len(poly), x), 5)
        r2 = round(horner(poly2, len(poly2), x), 5)
        if (r2 == 0):
            print("Division by 0")
            return 84
        while (x < 1.001):
            r1 = round(horner(poly, len(poly), x), 5)
            r2 = round(horner(poly2, len(poly2), x), 5)
            print("%.3f ->" % x, end= ' ')
            print("%.5f" % (r1 / r2))
            x = x + 0.001
            px.append(x)
            py.append(r1/r2)
            x = round(x, 3)
        #plt.plot(px, py)
        plt.scatter(px, py, color='b')
        plt.title('Courbe transfer')
        plt.xlabel('x')
        plt.ylabel('r1 / R2')
        plt.show()
    else:
        return 84