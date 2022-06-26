#!/usr/bin/env python3

import sys
import src
from src.args import *
from src.cmd import *

def main():
    args = sys.argv
    checklen(args)
    checkFunct(args[6])
    getCmd(args)

main()