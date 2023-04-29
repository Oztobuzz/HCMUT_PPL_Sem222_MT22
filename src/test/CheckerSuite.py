import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC
class CheckerSuite(unittest.TestCase):
        def test_jump1(self):
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
                expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"""
                self.assertTrue(TestChecker.test(input, expect, 101))

        def test_jump2(self):
                input = """
                main: function void() {
                        a: auto = f1(1,2,3) + 2;
                        x: string = true;
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"""
                self.assertTrue(TestChecker.test(input, expect, 102))

        def test_jump3(self):
                input = """
                main: function void() {
                        a: auto = {f1(1,2,3), 2};
                        x: string = true;
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"""
                self.assertTrue(TestChecker.test(input, expect, 103))

        def test_jump4(self):
                input = """
                main: function void() {
                        a: integer;
                        a = f1(1,2,3);
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"""
                self.assertTrue(TestChecker.test(input, expect, 104))

        def test_jump5(self):
                input = """
                main: function void() {
                        a: boolean = true;
                        a = f1(1,2,3);
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"""
                self.assertTrue(TestChecker.test(input, expect, 105))

        def test_dumb1(self):
                input = """
                f1: function void() {
                        x: auto = x + x;
                        x = 12;
                }
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 106))

        def test_dumb2(self):
                input = """
                main: function void(b: auto, c: auto) {
                        a: string = b + c;
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"""
                self.assertTrue(TestChecker.test(input, expect, 107))

        def test_dumb3(self):
                input = """
                main: function auto(x: float, y: float, z: float) {
                        return 1;
                        return "abc";
                        return true;
                        a: string = true;
                }
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 108))

        def test_dumb4(self):
                input = """
                main: function void(b: auto, c: auto) {
                        x: auto = x + 10;
                        y: string;
                        y = b * c;
                }
                """
                expect = """Type mismatch in statement: AssignStmt(Id(y), BinExpr(*, Id(b), Id(c)))"""
                self.assertTrue(TestChecker.test(input, expect, 109))

        def test_dumb5(self):
                input = """
                f1: function auto() {
                        if (true) {
                        return 1;
                        return "abc";
                        }
                        else return 2;
                        
                        return true;
                        return "abc";
                }
                """
                expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
                self.assertTrue(TestChecker.test(input, expect, 110))

        def test_superDumb(self):
                input = """
                f1: function auto(b: float, c: auto) {
                        do {
                        x: integer = 1;
                        } while (x + 1);
                }
                """
                expect = """Undeclared Identifier: x"""
                self.assertTrue(TestChecker.test(input, expect, 111))

        def test_superDumb2(self):
                input = """
                f1: function auto(b: float, c: auto) {
                        do {
                        x: integer = "abc";
                        } while (x + 1 == 2);
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(abc))"""
                self.assertTrue(TestChecker.test(input, expect, 112))

        def test_superDumb3(self):
                input = """
                f1: function auto(b: float, c: auto) {
                        do {
                        x: integer = "abc";
                        } while (x + 1);
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(abc))"""
                self.assertTrue(TestChecker.test(input, expect, 113))
        def test_anewthing(self):
                input =Program([VarDecl("a", IntegerType()), VarDecl("c", FloatType())])
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 114))
        
        def test_jump1(self):
                input = """
                main: function void() {
                a : array[3] of integer = {1_2, 2, 3};
                a : boolean = {a+b, _40 == c, !false, "string\\nline"};
        
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Redeclared Variable: a"""
                self.assertTrue(TestChecker.test(input, expect, 115))
        def test_arralit1(self):
                input = """
                main: function void() {
                a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};
                a : boolean = {a+b, _40 == c, !false, "string\\nline"};
        
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Redeclared Variable: a"""
                self.assertTrue(TestChecker.test(input, expect, 116))
        def test_arralit2(self):
                input = """
                main: function void() {
                a : array[2,3] of integer = {{1,2.0,5},{1.0 ,2, 3}};
                a : boolean = {a+b, _40 == c, !false, "string\\nline"};
        
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.0), IntegerLit(5)])"""
                self.assertTrue(TestChecker.test(input, expect, 117))
        def test_stmt_118(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 118))
        def test_stmt_119(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Invalid statement in function: VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"""
                self.assertTrue(TestChecker.test(input, expect, 119))
        def test_stmt_120(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void(pa2: integer) inherit foo {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Invalid Parameter: pa2"""
                self.assertTrue(TestChecker.test(input, expect, 120))
        def test_stmt_121(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void(pa1: integer) inherit foo {super(1,2);}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Invalid statement in function: VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"""
                self.assertTrue(TestChecker.test(input, expect, 121))
        def test_stmt_122(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void(pa1: integer) inherit foo {super("anc",2);}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Type mismatch in statement: CallStmt(foo, StringLit(anc), IntegerLit(2))"""
                self.assertTrue(TestChecker.test(input, expect, 122))
        def test_stmt_123(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {preventdefault() ;a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Undeclared Function: preventdefault"""
                self.assertTrue(TestChecker.test(input, expect, 123))
        def test_stmt_124(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {preventDefault() ;a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 124))
        def test_stmt_125(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {preventDefault() ;bar : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 125))
        def test_basicUndeclared_Identifier(self):
                input = Program([
        FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType(), IntegerLit(65)), AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
        ])    
        # expect = """main: function void () {
        #     a: integer = 65; 
        #     a = a + b;
        # }"""
                expect = "Undeclared Identifier: b"
                self.assertTrue(TestChecker.test(input, expect, 126))
        def test_basicUndeclared_Identifier_Param(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                FuncDecl("bds", IntegerType(), [ParamDecl("a", IntegerType()), ParamDecl("b", IntegerType(), inherit=True)], None, BlockStmt([ReturnStmt(Id("a"))])),
                FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = ""
                self.assertTrue(TestChecker.test(input, expect, 127))
        def test_basicCallStmt(self):
                """Test basicUndeclared_Function"""
                input = Program([
        	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt("helloWorld",[])]))
        ])
                expect = "Undeclared Function: helloWorld"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 202))
        def test_basic(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", IntegerType(), IntegerLit(1)),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
        VarDecl("x", IntegerType(), IntegerLit(65))
        ])
                expect = "Redeclared Variable: x"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 128))
        def test_basic2(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", IntegerType(), IntegerLit(1)),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
                VarDecl("a", IntegerType(), BinExpr("+", FloatLit(3) , IntegerLit(3)))
        ])
                expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(3), IntegerLit(3)))"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 129))
        def test_Binexpr(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", AutoType()),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
        VarDecl("a", AutoType(), BinExpr("+", Id("x") , IntegerLit(3)))
        ])
                expect = "Invalid Variable: x"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 130))
        def test_Unaryexpr(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
                VarDecl("a", AutoType(), UnExpr("!",BooleanLit(4))),
                VarDecl("b", AutoType(), UnExpr("!",IntegerLit(4)))
        ])
                expect = "Type mismatch in expression: UnExpr(!, IntegerLit(4))"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 131))
        def test_basicRedeclared_Identifier_Func_Param(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                FuncDecl("bds", IntegerType(), [ParamDecl("a", IntegerType()),ParamDecl("k", IntegerType()), ParamDecl("a", IntegerType(), inherit=True)], None, BlockStmt([ReturnStmt(Id("a"))])),
                FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = "Redeclared Parameter: a"
                self.assertTrue(TestChecker.test(input, expect, 132))
        def test_basicArrayLit(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                VarDecl("x", AutoType(),ArrayLit([IntegerLit(1), IntegerLit(2),  UnExpr("-",IntegerLit(4))]))])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = "No entry point"
                self.assertTrue(TestChecker.test(input, expect, 133))
        def test_identifier_134(self):
                input = """a: string = z;
        a,b,c : float = 1,2,3;
        a,b,c,d: boolean = a+b, 2==3, !true, arr[0,2];
        """
                expect = """Undeclared Identifier: z"""
                self.assertTrue(TestChecker.test(input, expect, 134))
        def test_identifier_135(self):
                input = """a: string = "abc";
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a+b, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: BinExpr(+, Id(a), Id(b))"""
                self.assertTrue(TestChecker.test(input, expect, 135))
        def test_identifier_136(self):
                input = """a: string = "abc";
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a==3, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: BinExpr(==, Id(a), IntegerLit(3))"""
                self.assertTrue(TestChecker.test(input, expect, 136))
        def test_identifier_137(self):
                input = """a: boolean = true;
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a==3, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])"""
                self.assertTrue(TestChecker.test(input, expect, 137))
        def test_specialfunc_138(self):
                input = """
    testfunc: function integer (c: string) {
        do {
            readString("abc");
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
                expect = """Type mismatch in statement: CallStmt(readString, StringLit(abc))"""
                self.assertTrue(TestChecker.test(input, expect, 138))
        def test_specialfunc_139(self):
                input = """
    testfunc: function integer (c: string) {
        do {
            readString();
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
                expect = """Type mismatch in expression: BinExpr(!=, Id(c), StringLit())"""
                self.assertTrue(TestChecker.test(input, expect, 139))
        def test_specialfunc_140(self):
                input = """
    testfunc: function integer (c: string) {
        do {
            readString();
            c = c :: "abc";
            printString(c);
        } while (4 != true );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
                expect = """Type mismatch in statement: CallStmt(testfunc, )"""
                self.assertTrue(TestChecker.test(input, expect, 140))
        def test_specialfunc_141(self):
                input = """
        foo:function auto() {
            return 123_323_3.e-23;
        }
        bar: function float() {
            return foo();
        }
        main:function void(){
            a: integer = 23%2+23-33_2%90;
            z: boolean = true && false;
            b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
            printInteger(a);
            writeFloat(b);
            if(z==true) {
                print("TRUE");
            }
            return;
        }
        """
                expect = """Undeclared Function: print"""
                self.assertTrue(TestChecker.test(input, expect, 141))
        def test_specialfunc_142(self):
                input = """
        foo:function integer() {
            return 123_323_3.e-23;
        }
        bar: function float() {
            return foo();
        }
        main:function void(){
            a: integer = 23%2+23-33_2%90;
            z: boolean = true && false;
            b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
            printInteger(a);
            writeFloat(b);
            if(z==true) {
                print("TRUE");
            }
            return;
        }
        """
                expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.233233e-17))"""
                self.assertTrue(TestChecker.test(input, expect, 142))
        def test_specialfunc_143(self):
                input = """
        foo:function auto() {
            return 123_323_3.e-23;
        }
        bar: function float() {
            return foo();
        }
        main:function void(){
            a: integer = 23%2+23-33_2%90;
            z: boolean = true && false;
            b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
            printInteger(a);
            writeFloat(b);
            return;
        }
        """
                expect = """"""
                self.assertTrue(TestChecker.test(input, expect, 143))
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

        def test_jump145(self):
                input = """
                main: function void() {
                        a: auto = f1(1,2,3) + 2;
                        x: string = true;
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"""
                self.assertTrue(TestChecker.test(input, expect, 145))

        def test_jump146(self):
                input = """
                main: function void() {
                        a: auto = {f1(1,2,3), 2};
                        x: string = true;
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"""
                self.assertTrue(TestChecker.test(input, expect, 146))

        def test_jump147(self):
                input = """
                main: function void() {
                        a: integer;
                        a = f1(1,2,3);
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"""
                self.assertTrue(TestChecker.test(input, expect, 147))

        def test_jump148(self):
                input = """
                main: function void() {
                        a: boolean = true;
                        a = f1(1,2,3);
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"""
                self.assertTrue(TestChecker.test(input, expect, 148))

        def test_dumb149(self):
                input = """
                f1: function void() {
                        x: auto = x + x;
                        x = 12;
                }
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 149))

        def test_dumb150(self):
                input = """
                main: function void(b: auto, c: auto) {
                        a: string = b + c;
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"""
                self.assertTrue(TestChecker.test(input, expect, 150))

        def test_dumb151(self):
                input = """
                main: function auto(x: float, y: float, z: float) {
                        return 1;
                        return "abc";
                        return true;
                        a: string = true;
                }
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 151))

        def test_dumb152(self):
                input = """
                main: function void(b: auto, c: auto) {
                        x: auto = x + 10;
                        y: string;
                        y = b * c;
                }
                """
                expect = """Type mismatch in statement: AssignStmt(Id(y), BinExpr(*, Id(b), Id(c)))"""
                self.assertTrue(TestChecker.test(input, expect, 152))

        def test_dumb153(self):
                input = """
                Pleasesaveme: function auto() {
                        return true;
                        return "abc";
                }
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 153))

        def test_superDumb154(self):
                input = """
                f1: function auto(b: float, c: auto) {
                        do {
                        Iamsotired: integer = 1;
                        } while (x + 1);
                }
                """
                expect = """Undeclared Identifier: x"""
                self.assertTrue(TestChecker.test(input, expect, 154))

        def test_superDumb155(self):
                input = """
                fico: function auto(b: float, c: auto) {
                        do {
                        z: integer = "rasputin";
                        } while (z + 1 != 2);
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(z, IntegerType, StringLit(rasputin))"""
                self.assertTrue(TestChecker.test(input, expect, 155))

        def test_superDumb156(self):
                input = """
                Itsgonnaend: function auto(b: float, c: auto) {
                        do {
                        x: integer = "abc";
                        } while (x + 1);
                }
                """
                expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(abc))"""
                self.assertTrue(TestChecker.test(input, expect, 156))
        def test_anewthing157(self):
                input =Program([VarDecl("a", IntegerType()), VarDecl("c", FloatType())])
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 157))
        
        def test_jump158(self):
                input = """
                main: function void() {
                a : array[3] of integer = {1_2, 2, 3};
                a : boolean = {a+b, _40 == c, !false, "string\\nline"};
        
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Redeclared Variable: a"""
                self.assertTrue(TestChecker.test(input, expect, 158))
        def test_arralit159(self):
                input = """
                main: function void() {
                a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};
                a : boolean = {a+b, _40 == c, !false, "string\\nline"};
        
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Redeclared Variable: a"""
                self.assertTrue(TestChecker.test(input, expect, 159))
        def test_arralit160(self):
                input = """
                main: function void() {
                a : array[2,3] of integer = {{1,2.0,5},{1.0 ,2, 3}};
                a : boolean = {a+b, _40 == c, !false, "string\\nline"};
        
                }
                f1: function auto(x: float, y: float, z: float) {
                        return x + y + z;
                }
                """
                expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.0), IntegerLit(5)])"""
                self.assertTrue(TestChecker.test(input, expect, 160))
        def test_stmt_161(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 151))
        def test_stmt_162(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Invalid statement in function: VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"""
                self.assertTrue(TestChecker.test(input, expect, 162))
        def test_stmt_163(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void(pa2: integer) inherit foo {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Invalid Parameter: pa2"""
                self.assertTrue(TestChecker.test(input, expect, 163))
        def test_stmt_164(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void(pa1: integer) inherit foo {super(1,2);}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Invalid statement in function: VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"""
                self.assertTrue(TestChecker.test(input, expect, 164))
        def test_stmt_165(self):
                input = """
                func: function integer(pa1 : float) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto(pa1 : float, inherit pa2:auto) {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void(pa1: integer) inherit foo {super("anc",2);}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Type mismatch in statement: CallStmt(foo, StringLit(anc), IntegerLit(2))"""
                self.assertTrue(TestChecker.test(input, expect, 165))
        def test_stmt_167(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {preventdefault() ;a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """Undeclared Function: preventdefault"""
                self.assertTrue(TestChecker.test(input, expect, 167))
        def test_stmt_168(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {preventDefault() ;a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 168))
        def test_stmt_169(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {preventDefault() ;bar : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 169))
        def test_basicUndeclared_Identifier_170(self):
                input = Program([
        FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType(), IntegerLit(65)), AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
        ])    
        # expect = """main: function void () {
        #     a: integer = 65; 
        #     a = a + b;
        # }"""
                expect = "Undeclared Identifier: b"
                self.assertTrue(TestChecker.test(input, expect, 170))
        def test_basicUndeclared_Identifier_Param_171(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                FuncDecl("bds", IntegerType(), [ParamDecl("a", IntegerType()), ParamDecl("b", IntegerType(), inherit=True)], None, BlockStmt([ReturnStmt(Id("a"))])),
                FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = ""
                self.assertTrue(TestChecker.test(input, expect, 171))
        #     def test_basicCallStmt(self):
        #         """Test basicUndeclared_Function"""
        #         input = Program([
        # 	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt("helloWorld",[])]))
        # ])
        #         expect = "Undeclared Function: helloWorld"
        # # main: function void () {
        # #                 helloWorld(); 
        # #         }
        #         self.assertTrue(TestChecker.test(input, expect, 403))
        def test_basic_172(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", IntegerType(), IntegerLit(1)),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
        VarDecl("x", IntegerType(), IntegerLit(65))
        ])
                expect = "Redeclared Variable: x"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 172))
        def test_basic_173(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", IntegerType(), IntegerLit(1)),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
                VarDecl("a", IntegerType(), BinExpr("+", FloatLit(3) , IntegerLit(3)))
        ])
                expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(3), IntegerLit(3)))"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 173))
        def test_Binexpr_174(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", AutoType()),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
        VarDecl("a", AutoType(), BinExpr("+", Id("x") , IntegerLit(3)))
        ])
                expect = "Invalid Variable: x"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 174))
        def test_Unaryexpr_175(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
                VarDecl("a", AutoType(), UnExpr("!",BooleanLit(4))),
                VarDecl("b", AutoType(), UnExpr("!",IntegerLit(4)))
        ])
                expect = "Type mismatch in expression: UnExpr(!, IntegerLit(4))"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 175))
        def test_basicRedeclared_Identifier_Func_Param_176(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                FuncDecl("bds", IntegerType(), [ParamDecl("a", IntegerType()),ParamDecl("k", IntegerType()), ParamDecl("a", IntegerType(), inherit=True)], None, BlockStmt([ReturnStmt(Id("a"))])),
                FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = "Redeclared Parameter: a"
                self.assertTrue(TestChecker.test(input, expect, 176))
        def test_basicArrayLit_177(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                VarDecl("x", AutoType(),ArrayLit([IntegerLit(1), IntegerLit(2),  UnExpr("-",IntegerLit(4))]))])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = "No entry point"
                self.assertTrue(TestChecker.test(input, expect, 177))
        def test_identifier_178(self):
                input = """a: string = z;
        a,b,c : float = 1,2,3;
        a,b,c,d: boolean = a+b, 2==3, !true, arr[0,2];
        """
                expect = """Undeclared Identifier: z"""
                self.assertTrue(TestChecker.test(input, expect, 178))
        def test_identifier_179(self):
                input = """a: string = "abc";
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a+b, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: BinExpr(+, Id(a), Id(b))"""
                self.assertTrue(TestChecker.test(input, expect, 179))
        def test_identifier_180(self):
                input = """a: string = "abc";
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a==3, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: BinExpr(==, Id(a), IntegerLit(3))"""
                self.assertTrue(TestChecker.test(input, expect, 180))
        def test_identifier_181(self):
                input = """a: boolean = true;
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a==3, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])"""
                self.assertTrue(TestChecker.test(input, expect, 181))
        def test_specialfunc_182(self):
                input = """
    testfunc: function integer (c: string) {
        do {
            readString("abc");
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
                expect = """Type mismatch in statement: CallStmt(readString, StringLit(abc))"""
                self.assertTrue(TestChecker.test(input, expect, 182))
        def test_specialfunc_183(self):
                input = """
    testfunc: function integer (c: string) {
        do {
            readString();
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
                expect = """Type mismatch in expression: BinExpr(!=, Id(c), StringLit())"""
                self.assertTrue(TestChecker.test(input, expect, 183))
        def test_specialfunc_184(self):
                input = """
    testfunc: function integer (c: string) {
        do {
            readString();
            c = c :: "abc";
            printString(c);
        } while (4 != true );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
                expect = """Type mismatch in statement: CallStmt(testfunc, )"""
                self.assertTrue(TestChecker.test(input, expect, 184))
        def test_specialfunc_185(self):
                input = """
        foo:function auto() {
            return 123_323_3.e-23;
        }
        bar: function float() {
            return foo();
        }
        main:function void(){
            a: integer = 23%2+23-33_2%90;
            z: boolean = true && false;
            b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
            printInteger(a);
            writeFloat(b);
            if(z==true) {
                print("TRUE");
            }
            return;
        }
        """
                expect = """Undeclared Function: print"""
                self.assertTrue(TestChecker.test(input, expect, 185))
        def test_specialfunc_186(self):
                input = """
        foo:function integer() {
            return 123_323_3.e-23;
        }
        bar: function float() {
            return foo();
        }
        main:function void(){
            a: integer = 23%2+23-33_2%90;
            z: boolean = true && false;
            b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
            printInteger(a);
            writeFloat(b);
            if(z==true) {
                print("TRUE");
            }
            return;
        }
        """
                expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.233233e-17))"""
                self.assertTrue(TestChecker.test(input, expect, 186))
        def test_specialfunc_187(self):
                input = """
        foo:function auto() {
            return 123_323_3.e-23;
        }
        bar: function float() {
            return foo();
        }
        main:function void(){
            a: integer = 23%2+23-33_2%90;
            z: boolean = true && false;
            b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
            printInteger(a);
            writeFloat(b);
            return;
        }
        """
                expect = """"""
                self.assertTrue(TestChecker.test(input, expect, 187))
        def test_stmt_188(self):
                input = """
                func: function integer() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foo: function auto() {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                bar: function void() inherit foo {preventDefault() ;bar : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                foobar: function array[1_2] of float () inherit bar {a : array[2,3] of integer = {{1,2,5},{1 ,2, 3}};}
                """
                expect = """No entry point"""
                self.assertTrue(TestChecker.test(input, expect, 188))
        def test_basicUndeclared_Identifier_189(self):
                input = Program([
        FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType(), IntegerLit(65)), AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
        ])    
        # expect = """main: function void () {
        #     a: integer = 65; 
        #     a = a + b;
        # }"""
                expect = "Undeclared Identifier: b"
                self.assertTrue(TestChecker.test(input, expect, 189))
        def test_basicUndeclared_Identifier_Param_190(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                FuncDecl("bds", IntegerType(), [ParamDecl("a", IntegerType()), ParamDecl("b", IntegerType(), inherit=True)], None, BlockStmt([ReturnStmt(Id("a"))])),
                FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = ""
                self.assertTrue(TestChecker.test(input, expect, 190))
        #     def test_basicCallStmt(self):
        #         """Test basicUndeclared_Function"""
        #         input = Program([
        # 	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt("helloWorld",[])]))
        # ])
        #         expect = "Undeclared Function: helloWorld"
        # # main: function void () {
        # #                 helloWorld(); 
        # #         }
        #         self.assertTrue(TestChecker.test(input, expect, 403))
        def test_basic_191(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", IntegerType(), IntegerLit(1)),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
        VarDecl("x", IntegerType(), IntegerLit(65))
        ])
                expect = "Redeclared Variable: x"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 191))
        def test_basic_192(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", IntegerType(), IntegerLit(1)),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
                VarDecl("a", IntegerType(), BinExpr("+", FloatLit(3) , IntegerLit(3)))
        ])
                expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(3), IntegerLit(3)))"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 192))
        def test_Binexpr_193(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("x", AutoType()),
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
        VarDecl("a", AutoType(), BinExpr("+", Id("x") , IntegerLit(3)))
        ])
                expect = "Invalid Variable: x"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 193))
        def test_Unaryexpr_194(self):
                """Test basicUndeclared_Function"""
                input = Program([
                VarDecl("y", IntegerType(), IntegerLit(2)),
                VarDecl("z", IntegerType(), IntegerLit(3)),
                VarDecl("a", AutoType(), UnExpr("!",BooleanLit(4))),
                VarDecl("b", AutoType(), UnExpr("!",IntegerLit(4)))
        ])
                expect = "Type mismatch in expression: UnExpr(!, IntegerLit(4))"
        # main: function void () {
        #                 helloWorld(); 
        #         }
                self.assertTrue(TestChecker.test(input, expect, 194))
        def test_basicRedeclared_Identifier_Func_Param_195(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                FuncDecl("bds", IntegerType(), [ParamDecl("a", IntegerType()),ParamDecl("k", IntegerType()), ParamDecl("a", IntegerType(), inherit=True)], None, BlockStmt([ReturnStmt(Id("a"))])),
                FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = "Redeclared Parameter: a"
                self.assertTrue(TestChecker.test(input, expect, 195))
        def test_basicArrayLit_196(self):
                """Test basicUndeclared_Identifier_Param"""
                input = Program([
                VarDecl("x", AutoType(),ArrayLit([IntegerLit(1), IntegerLit(2),  UnExpr("-",IntegerLit(4))]))])
                #  """
                #     bds: function integer () {
                #         return a; 
                #     }
                #     main: function void () {
                # }"""
        
                expect = "No entry point"
                self.assertTrue(TestChecker.test(input, expect, 196))
        def test_identifier_197(self):
                input = """a: string = z;
        a,b,c : float = 1,2,3;
        a,b,c,d: boolean = a+b, 2==3, !true, arr[0,2];
        """
                expect = """Undeclared Identifier: z"""
                self.assertTrue(TestChecker.test(input, expect, 197))
        def test_identifier_198(self):
                input = """a: string = "abc";
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a+b, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: BinExpr(+, Id(a), Id(b))"""
                self.assertTrue(TestChecker.test(input, expect, 198))
        def test_identifier_199(self):
                input = """a: string = "abc";
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a==3, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: BinExpr(==, Id(a), IntegerLit(3))"""
                self.assertTrue(TestChecker.test(input, expect, 199))
        def test_identifier_200(self):
                input = """a: boolean = true;
        d,b,c : float = 1,2,3;
        aa,bb,cc,dd: boolean = a==3, 2==3, !true, arr[0,2];
        """
                expect = """Type mismatch in expression: ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])"""
                self.assertTrue(TestChecker.test(input, expect, 200))
        def test_specialfunc_201(self):
                input = """
    testfunc: function integer (c: string) {
        do {
            readString("abc");
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
                expect = """Type mismatch in statement: CallStmt(readString, StringLit(abc))"""
                self.assertTrue(TestChecker.test(input, expect, 201))
 