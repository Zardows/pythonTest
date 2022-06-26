#!/usr/bin/env python3

import unittest
import sys
from src import *
from src.args import *
from src.cmd import *

class Test_erroryams(unittest.TestCase):

    def test_invalid_dice(self):
        sys.argv = "./201yams 1 2 3 4 7 pair_5"
        with self.assertRaises(SystemExit) as cm:
            check_args(sys.argv)
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument(self):
        sys.argv = "./201yams 1 2 3 4 pair_5"
        with self.assertRaises(SystemExit) as cm:
            checklen(sys.argv)
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_instruction(self):
        sys.argv = "./201yams 1 2 3 4 5 pai_5"
        with self.assertRaises(SystemExit) as cm:
            checkFunct(sys.argv)
        self.assertEqual(cm.exception.code, 84)

    def test_bigger_than_six(self):
        sys.argv = "./201yams 1 2 3 4 5 pair_7"
        with self.assertRaises(SystemExit) as cm:
            checkFunct(sys.argv)
        self.assertEqual(cm.exception.code, 84)

    def test_smallerr_than_1(self):
        sys.argv = "./201yams 1 2 3 4 5 pair_0"
        with self.assertRaises(SystemExit) as cm:
            checkFunct(sys.argv)
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument_pair(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("pair", 2, ["oui", "4"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument_three(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("three", 2, ["oui", "4"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument_four(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("four", 2, ["oui", "4"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument_straight(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("straight", 2, ["oui", "4"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument_yams(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("yams", 2, ["oui", "4"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument_full(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("full", 3, ["oui", "4"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_number_of_argument_full_two(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("full", 1, ["oui", "4"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_argument_straight(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("straight", 1, ["oui", "3"])
        self.assertEqual(cm.exception.code, 84)

    def test_invalid_argument_straight_two(self):
        with self.assertRaises(SystemExit) as cm:
            checkFuncArgument("full", 1, ["oui", "7"])
        self.assertEqual(cm.exception.code, 84)

    def test_not_digit(self):
        with self.assertRaises(SystemExit) as cm:
            checkDigit(["A", "2", "3"], 0)
        self.assertEqual(cm.exception.code, 84)

class Test_function(unittest.TestCase):
    def test_yams_res(self):
        print("test_yams_res : OK")
        self.assertEqual(round(calcProba(4, [0, 0, 0, 0, 0], 5), 2), 0.01)

    def test_yams_res_c(self):
        print("test_yams_res_c : OK")
        self.assertEqual(round(calcProba(4, [4, 4, 4, 4, 4], 5), 2), 100.00)

    def test_four_res(self):
        print("test_four_res : OK")
        self.assertEqual(round(calcProba(4, [1, 2, 3, 4, 5], 4), 2), 1.62)

    def test_four_res_c(self):
        print("test_four_res_c : OK")
        self.assertEqual(round(calcProba(4, [4, 4, 4, 4, 5], 4), 2), 100.00)

    def test_straight_res(self):
        print("test_straight_res : OK")
        self.assertEqual(round(calcStraight(6, [2, 2, 5, 4, 6]), 2), 16.67)

    def test_straight_res_c(self):
        print("test_straight_c_res : OK")
        self.assertEqual(round(calcStraight(6, [2, 3, 4, 5, 6]), 2), 100.00)

    def test_full_res(self):
        print("test_full_res : OK")
        self.assertEqual(round(calcFull(2, 3, [0, 0, 0, 0, 0]), 2), 0.13)

    def test_full_res_c(self):
        print("test_full_res_c : OK")
        self.assertEqual(round(calcFull(2, 3, [2, 3, 2, 3, 2]), 2), 100.00)

    def test_pair_res_c(self):
        print("test_pair_res_c : OK")
        self.assertEqual(round(calcProba(2, [2, 3, 2, 3, 2], 2), 2), 100.00)

    def test_three_res_c(self):
        print("test_three_res_c : OK")
        self.assertEqual(round(calcProba(2, [2, 3, 2, 3, 2], 3), 2), 100.00)

if __name__ == '__main__':
    unittest.main()