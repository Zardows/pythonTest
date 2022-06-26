#!/usr/bin/env python3

import sys
import math

class IQ:
    def do_usage(self):
        print("USAGE")
        print("    ./205IQ u s [IQ1] [IQ2]\n")
        print("DESCRIPTION")
        print("    u      mean")
        print("    s      standard deviation")
        print("    IQ1      minimum IQ")
        print("    IQ2      maximum IQ")
        sys.exit(0)

    def print_error(self, str):
        print(str)
        sys.exit(84)

    def inf_calc(self, mic, sig, q1):
        res = 0
        i = 0
        while i < int(q1):
            res += (1 / (sig * math.sqrt(2*math.pi))) * (math.exp(-((pow(i - mic, 2)) / (2 * pow(sig, 2)))))
            i = i + 0.001
        res /= 10
        print(str(round(res, 1)) + "%" + " of people have an IQ inferior to " + str(int(q1)))

    def between_calc(self, mic, sig, q1, q2):
        res = 0
        i = int(q1)
        while i < int(q2):
            res += (1 / (sig * math.sqrt(2*math.pi))) * (math.exp(-((pow(i - mic, 2)) / (2 * pow(sig, 2)))))
            i = i + 0.001
        res /= 10
        print(str(round(res, 1)) + "%" + " of people have an IQ between " + str(int(q1)) + " and " + str(int(q2)))

    def print_plot(self, mic, sig):
        res = 0
        for i in range(0, 201):
            res = (1 / (sig * math.sqrt(2*math.pi))) * (math.exp(-((pow(i - mic, 2)) / (2 * pow(sig, 2)))))
            #st = (str(round(res, 5) - int(round(res, 5))))
            #while (len(st) != 7):
             #   st = st + "0"
            print(i, '{0:.5f}'.format((res)))

    def check_args(self, arg):
        for i in range(0, len(arg)):
            if ((arg[i]) < '0' or (arg[i]) > '9') and arg[i] != '.':
                print("ERROR: invalid argument")
                sys.exit(84)
        return float(arg)

    def get_value(self, args):
        tab = []
        l = len(args)
        if (l == 2 and args[1] == "-h"):
            self.do_usage()
        if (l >= 3 and l <= 5):
            tab.append(self.check_args(args[1]))
            tab.append(self.check_args(args[2]))
            if (l >= 4):
                tab.append(self.check_args(args[3]))
            if (l == 5):
                tab.append(self.check_args(args[4]))
            return tab
        else:
            print("ERROR : Invalid number of arguments")
            sys.exit(84)


    def checklen(self, args):
        val = self.get_value(args)
        if (len(val) == 3 and (val[2] < 0 or val[2] > 200)):
            print("ERROR: invalid IQ")
            sys.exit(84)
        if (len(val) == 4 and val[2] > val[3]):
            print("ERROR: IQ1 must be inferior to IQ2")
            sys.exit(84)
        if (len(val) == 4) and (val[2] < 0 or val[3] > 200):
            print("ERROR: invalid IQ")
            sys.exit(84)
        if val[0] < 0 or val[0] > 200 or val[1] < 0 or val[1] > 200:
            print("ERROR: invalid arg")
            sys.exit(84) 
        if int(val[0]) == 0:
            self.print_error("ERROR: division by 0")
        if len(args) == 3:
            self.print_plot(val[0], val[1])
        if len(args) == 4:
            self.inf_calc(val[0], val[1], val[2])
        if len(args) == 5:
            self.between_calc(val[0], val[1], val[2], val[3])
        
    def main(self):
        args = sys.argv
        self.checklen(args)

x = IQ()
x.main()