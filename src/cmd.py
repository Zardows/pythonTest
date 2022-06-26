#!/usr/bin/env python3

from math import *

def print_res(str, cmd, res):
    print("Chances to get a", str, cmd + ": %.2f" % res + "%")

def coeff(n, k):
    res = factorial(n) / (factorial(k) * (factorial(n - k)))
    return res

def binomial(n, k):
    res = coeff(n, k) * pow((1/6), k) * pow((1 - 1/6), (n - k))
    return res

def calcProba(nb, dices, arg):
    keep = 5 - (5 - dices.count(int(nb)))
    res = 0
    if keep < arg:
        for n in range(arg - keep, 6 - keep):
            res += binomial(5 - keep, n)
        res *= 100
    else:
        res = 100
    return res

def calcFull(first, second, dices):
    keepFirst = 5 - (5 - dices.count(int(first)))
    keepSecond = 5 - (5 - dices.count(int(second)))

    if (keepFirst == 3 and keepSecond == 2):
        return 100
    if keepFirst > 3:
        keepFirst = 3
    if keepSecond > 2:
        keepSecond = 2
    nb = 5 - keepFirst - keepSecond
    if nb == 1:
        return 1/6 * 100
    else:
        pair = (factorial(3 - keepFirst) / factorial(3 - keepFirst))
        three = (factorial(2 - keepSecond) / factorial(2 - keepSecond))
        return ((pair * three) / pow(6, nb)) * 1000

def calcStraight(nb, args):
    args = sorted(list(set(args)), reverse=True)
    dice = 0
    liste = [1, 2, 3, 4, 5, 6]
    nb = int(nb)
    x = 5
    while x > 0:
        if nb in args:
            dice += 1
        nb -= 1
        x -= 1
    return (factorial(5 - dice) / pow(6, 5 - dice) * 100)

def otherCmd(exec, args):
    if exec[0] == "yams":
        print_res(str(exec[1]), "yams", calcProba(exec[1], args, 5))
    if exec[0] == "full":
        print_res(str(exec[1]), "full of " + str(exec[2]), calcFull(exec[1], exec[2], args))
    if exec[0] == "straight":
        print_res(str(exec[1]), "straight", calcStraight(exec[1], args))

def getCmd(args):
    exec = args[6].split('_')
    args.pop(0)
    args.pop(5)
    args = [int(x) for x in args]
    if exec[0] == "pair":
        print_res(str(exec[1]), "pair", calcProba(exec[1], args, 2))
    if exec[0] == "three":
        print_res(str(exec[1]), "three-of-a-kind", calcProba(exec[1], args, 3))
    if exec[0] == "four":
        print_res(str(exec[1]), "four-of-a-kind", calcProba(exec[1], args, 4))
    else:
        otherCmd(exec, args)
