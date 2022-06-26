#!/usr/bin/env python3

import sys

def do_usage():
    print("USAGE")
    print("    ./201yams d1 d2 d3 d4 d5 c\n")
    print("DESCRIPTION")
    print("    d1      value of the first die (0 if not thrown)")
    print("    d2      value of the second die (0 if not thrown)")
    print("    d3      value of the third die (0 if not thrown)")
    print("    d4      value of the fourth die (0 if not thrown)")
    print("    d5      value of the fifth die (0 if not thrown)")
    print("    c      expected combination")
    sys.exit(0)

def check_args(arg):
    i = 1
    while i < 6:
        if (arg[i]) < '0' or (arg[i]) > '6':
            print("ERROR: dice value must be between 0 and 6")
            sys.exit(84)
        i += 1

def checklen(args):
    if (len(args) == 2 and args[1] == "-h"):
        do_usage()
    if (len(args) == 7):
        check_args(args)
    else:
        print("ERROR : Invalid number of arguments")
        sys.exit(84)

def checkFunct(argCmd):
    cmd = argCmd.split('_')
    if len(cmd) - 1 > 2 or len(cmd) - 1 < 1:
        print("ERROR : invalid Command")
        sys.exit(84)
    func = cmd[0]
    checkDigit(cmd, 1)
    nb1 = int(cmd[1])
    if len(cmd) - 1 == 2:
        checkDigit(cmd, 2)
        nb2 = int(cmd[2])
        if nb2 < 1 or nb2 > 6:
            print("ERROR : " + str(nb2) + " is not inbetween 1 and 6")
            sys.exit(84)
    if nb1 < 1 or nb1 > 6:
        print("ERROR : " + str(nb1) + " is not inbetween 1 and 6")
        sys.exit(84)
    if (func != "pair" and func != "three" and func != "four"
        and func != "full" and func != "straight" and func != "yams"):
        print("ERROR : " + func + " is an invalid instruction")
        sys.exit(84)
    checkFuncArgument(func, len(cmd) - 1, cmd)

def checkFuncArgument(cmd, nbArg, arg):
    if (cmd == "full" and nbArg != 2):
        print("ERROR : full takes 2 arguments")
        sys.exit(84)
    if (cmd == "full" and (arg[2] == arg[1])):
        print("ERROR : cannot use the same number for a full")
        sys.exit(84)
    if (cmd == "straight" and (int(arg[1]) < 5 or int(arg[1]) > 6)):
        print("ERROR : straight argument must be inbetween 4 and 6")
        sys.exit(84)
    elif (cmd != "full" and nbArg != 1):
        print("ERROR : " + cmd + " takes only 1 argument")
        sys.exit(84)

def checkDigit(cmd, i):
    if cmd[i].isdigit() == False:
        print("ERROR : invalid command")
        sys.exit(84)