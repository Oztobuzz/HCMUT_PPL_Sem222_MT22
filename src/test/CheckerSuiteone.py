import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC
class CheckerSuite(unittest.TestCase):
#       def test_basicArrayLit(self):
#         """Test basicUndeclared_Identifier_Param"""
#         input = Program([
# 	VarDecl("x", ArrayType([3], FloatType()),ArrayLit([FloatLit(1), IntegerLit(2),  UnExpr("-",IntegerLit(4))]))])
#         #  """
#         #     bds: function integer () {
#         #         return a; 
#         #     }
#         #     main: function void () {
#         # }"""
 
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 409))
        def test_jump144(self):
                input = """
                main: function void() {
                        a: auto = {1, 2};
                        a[f1(1,2,3)] = 2;
                        x: string = true;
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"""
                self.assertTrue(TestChecker.test(input, expect, 144))