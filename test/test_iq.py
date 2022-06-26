#!/usr/bin/env python3

import unittest
import sys
from unittest.main import main
from src import *
from src.main import *

class Test_erroriq(unittest.TestCase):

    def test_too_few_args(self):
        sys.argv = ["./205IQ",  "5"]
        with self.assertRaises(SystemExit) as cm:
            x.main()
        self.assertEqual(cm.exception.code, 84)

    # def test_too_many_args(self):
    #     sys.argv = "./205IQ 5 4 6 7 9"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_letter_in_args(self):
    #     sys.argv = "./205IQ a 3"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_zero_fst(self):
    #     sys.argv = "./205IQ 0 4"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_neg_fst(self):
    #     sys.argv = "./205IQ -1 4"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_supp_fst(self):
    #     sys.argv = "./205IQ 201 4"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_neg_snd(self):
    #     sys.argv = "./205IQ 3 -1"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_supp_snd(self):
    #     sys.argv = "./205IQ 5 201"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_neg_third(self):
    #     sys.argv = "./205IQ 5 5 -1"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_sup_third(self):
    #     sys.argv = "./205IQ 5 4 201"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_neg_fourf(self):
    #     sys.argv = "./205IQ 5 4 5 -1"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_supp_fourf(self):
    #     sys.argv = "./205IQ 5 6 8 201"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

    # def test_biger_third(self):
    #     sys.argv = "./205IQ 5 4 15 10"
    #     with self.assertRaises(SystemExit) as cm:
    #         check_args(sys.argv)
    #     self.assertEqual(cm.exception.code, 84)

if __name__ == '__main__':
    unittest.main()