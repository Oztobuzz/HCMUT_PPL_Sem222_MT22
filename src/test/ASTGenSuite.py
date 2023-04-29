# //2053186
# //Le Hoang Long

import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer = 7.e2;"""
        expect = str(Program([VarDecl("x", IntegerLit())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
        main: function void () {
            printInteger(4, 2.3);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4), FloatLit(2.3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_arrlit(self):
        input = """main: function void () {
            a = {1,2,3};
            b = {1_1_1, 0, 1_0_1};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(Id(b), ArrayLit([IntegerLit(111), IntegerLit(0), IntegerLit(101)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_arrlit1(self):
        input = """main: function void () {
            a = {1.1, 2.0022, 1_2_3.003};
            b = {2e-2, 2.2e-2, .e2};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([FloatLit(1.1), FloatLit(2.0022), FloatLit(123.003)])), AssignStmt(Id(b), ArrayLit([FloatLit(0.02), FloatLit(0.022), FloatLit(0.0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_arrlit2(self):
        input = """main: function void () {
            a = {1+1, a<=b, !true, "string1"::"string\\"2\\""};
            b = {2e-2 * 1_1.E+3, a[2e-2 * 1_1.E+3]};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(<=, Id(a), Id(b)), UnExpr(!, BooleanLit(True)), BinExpr(::, StringLit(string1), StringLit(string\\"2\\"))])), AssignStmt(Id(b), ArrayLit([BinExpr(*, FloatLit(0.02), FloatLit(11000.0)), ArrayCell(a, [BinExpr(*, FloatLit(0.02), FloatLit(11000.0))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_arrlit3(self):
        input = """main: function void () {
            arrOfArr = { {1+1, a<=b}, {!true, "string1"::"string\\"2\\""}, {2e-2 * 1_1.E+3, a[2e-2 * 1_1.E+3]} };
            arrOfArrOfArr = { {{1+1, a<=b}, {!true, "string1"::"string\\"2\\""}} , {{2e-2 * 1_1.E+3, {a[2e-2 * 1_1.E+3]}}} };
            empArr =  {};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arrOfArr), ArrayLit([ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(<=, Id(a), Id(b))]), ArrayLit([UnExpr(!, BooleanLit(True)), BinExpr(::, StringLit(string1), StringLit(string\\"2\\"))]), ArrayLit([BinExpr(*, FloatLit(0.02), FloatLit(11000.0)), ArrayCell(a, [BinExpr(*, FloatLit(0.02), FloatLit(11000.0))])])])), AssignStmt(Id(arrOfArrOfArr), ArrayLit([ArrayLit([ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(<=, Id(a), Id(b))]), ArrayLit([UnExpr(!, BooleanLit(True)), BinExpr(::, StringLit(string1), StringLit(string\\"2\\"))])]), ArrayLit([ArrayLit([BinExpr(*, FloatLit(0.02), FloatLit(11000.0)), ArrayLit([ArrayCell(a, [BinExpr(*, FloatLit(0.02), FloatLit(11000.0))])])])])])), AssignStmt(Id(empArr), ArrayLit([]))]))
])"""

    def test_vardecl(self):
        input = """main: function void () {
            a: integer;
            _bc: float;
            ___90: string;
            _____: boolean;
            String: auto;       //keyword vs ID
            ARRAY: array[0] of float;
            Array: array[1,2,3_1] of integer;
            arrAy: array[1_2_3] of string;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(_bc, FloatType), VarDecl(___90, StringType), VarDecl(_____, BooleanType), VarDecl(String, AutoType), VarDecl(ARRAY, ArrayType([0], FloatType)), VarDecl(Array, ArrayType([1, 2, 31], IntegerType)), VarDecl(arrAy, ArrayType([123], StringType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_vardecl1(self):
        input = """a, _bc, ___90: integer;
        a, ___, __c__: array[1_2, 2, 3] of string;
        """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(_bc, IntegerType)
	VarDecl(___90, IntegerType)
	VarDecl(a, ArrayType([12, 2, 3], StringType))
	VarDecl(___, ArrayType([12, 2, 3], StringType))
	VarDecl(__c__, ArrayType([12, 2, 3], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_vardecl2(self):
        input = """_var_ : auto = "string\\"Inner\\"";
        a, b, ___90 : integer = 1, a+b, a==b;
        """
        expect = """Program([
	VarDecl(_var_, AutoType, StringLit(string\\"Inner\\"))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, BinExpr(+, Id(a), Id(b)))
	VarDecl(___90, IntegerType, BinExpr(==, Id(a), Id(b)))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_vardecl3(self):
        input = """a : boolean = {1_2, .E-003, false, "string"};
        a : boolean = {a+b, _40 == c, !false, "string\\nline"};
        """
        expect = """Program([
	VarDecl(a, BooleanType, ArrayLit([IntegerLit(12), FloatLit(0.0), BooleanLit(False), StringLit(string)]))
	VarDecl(a, BooleanType, ArrayLit([BinExpr(+, Id(a), Id(b)), BinExpr(==, Id(_40), Id(c)), UnExpr(!, BooleanLit(False)), StringLit(string\\nline)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    
    def test_vardecl4(self):
        input = """a: string = z;
        a,b,c : float = 1,2,3;
        a,b,c,d: boolean = a+b, 2==3, !true, arr[0,2];
        """
        expect = """Program([
	VarDecl(a, StringType, Id(z))
	VarDecl(a, FloatType, IntegerLit(1))
	VarDecl(b, FloatType, IntegerLit(2))
	VarDecl(c, FloatType, IntegerLit(3))
	VarDecl(a, BooleanType, BinExpr(+, Id(a), Id(b)))
	VarDecl(b, BooleanType, BinExpr(==, IntegerLit(2), IntegerLit(3)))
	VarDecl(c, BooleanType, UnExpr(!, BooleanLit(True)))
	VarDecl(d, BooleanType, ArrayCell(arr, [IntegerLit(0), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_funcdecl(self):
        input = """
        func: function integer() {}
        foo: function auto() {}
        bar: function void() inherit foo {}
        foobar: function array[1_2] of float () inherit bar {}
        """
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([]))
	FuncDecl(foo, AutoType, [], None, BlockStmt([]))
	FuncDecl(bar, VoidType, [], foo, BlockStmt([]))
	FuncDecl(foobar, ArrayType([12], FloatType), [], bar, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_funcdecl1(self):
        input = """
        func: function string (pa1 : float){}
        func: function string (pa1 : float, inherit pa2:auto){}
        func: function string (pa1 : float, inherit pa2:auto, out pa3:string, inherit out pa4: array[2,3] of integer){}
        """
        expect = """Program([
	FuncDecl(func, StringType, [Param(pa1, FloatType)], None, BlockStmt([]))
	FuncDecl(func, StringType, [Param(pa1, FloatType), InheritParam(pa2, AutoType)], None, BlockStmt([]))
	FuncDecl(func, StringType, [Param(pa1, FloatType), InheritParam(pa2, AutoType), OutParam(pa3, StringType), InheritOutParam(pa4, ArrayType([2, 3], IntegerType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_funcdecl2(self):
        input = """func: function string (pa1 : float){
            a:integer = 0;
            b = a-1;
            return;
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [Param(pa1, FloatType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), AssignStmt(Id(b), BinExpr(-, Id(a), IntegerLit(1))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_funcdecl3(self):
        input = """func: function string (pa1 : float, out pa2: boolean){
            a:integer = pa1;
            if (a <= 3.E-2) return true;
            else {
                a = 0;
                return false;
            }
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [Param(pa1, FloatType), OutParam(pa2, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType, Id(pa1)), IfStmt(BinExpr(<=, Id(a), FloatLit(0.03)), ReturnStmt(BooleanLit(True)), BlockStmt([AssignStmt(Id(a), IntegerLit(0)), ReturnStmt(BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_funcdecl4(self):
        input = """func: function string (pa1 : float, out pa2: boolean){
            a:integer = pa1;
            while (a <= 3.E-2) {
                a = a + 1;
                if (a != 0) continue;
                else break;
            }
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [Param(pa1, FloatType), OutParam(pa2, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType, Id(pa1)), WhileStmt(BinExpr(<=, Id(a), FloatLit(0.03)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(!=, Id(a), IntegerLit(0)), ContinueStmt(), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_funcdecl5(self):
        input = """
        func: function string (pa1 : float, out pa2: boolean){
            a:integer = pa1;
            while (a <= 3.E-2) {
                a = a + 1;
                if (a != 0) continue;
                else break;
            }
        }
        arr: array[2, 2_2] of integer = {1.2, .E-004, false};
        func: function string (pa1 : float, out pa2: boolean){
            a:integer = pa1;
            if (a <= 3.E-2) return true;
            else {
                a = 0;
                return false;
            }
        }
        """
        expect = """Program([
	FuncDecl(func, StringType, [Param(pa1, FloatType), OutParam(pa2, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType, Id(pa1)), WhileStmt(BinExpr(<=, Id(a), FloatLit(0.03)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(!=, Id(a), IntegerLit(0)), ContinueStmt(), BreakStmt())]))]))
	VarDecl(arr, ArrayType([2, 22], IntegerType), ArrayLit([FloatLit(1.2), FloatLit(0.0), BooleanLit(False)]))
	FuncDecl(func, StringType, [Param(pa1, FloatType), OutParam(pa2, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType, Id(pa1)), IfStmt(BinExpr(<=, Id(a), FloatLit(0.03)), ReturnStmt(BooleanLit(True)), BlockStmt([AssignStmt(Id(a), IntegerLit(0)), ReturnStmt(BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_funcCall(self):
        input = """
        a: integer = foo(1);
        a: integer = bar(1, 2_2.e-02, false, "string");
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(foo, [IntegerLit(1)]))
	VarDecl(a, IntegerType, FuncCall(bar, [IntegerLit(1), FloatLit(0.22), BooleanLit(False), StringLit(string)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_funcCall1(self):
        input = """
        a: integer = bar(a,b,c, ar[1,2],arr[0,1_2], a+b, a==b);
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(bar, [Id(a), Id(b), Id(c), ArrayCell(ar, [IntegerLit(1), IntegerLit(2)]), ArrayCell(arr, [IntegerLit(0), IntegerLit(12)]), BinExpr(+, Id(a), Id(b)), BinExpr(==, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_funcCall2(self):
        input = """
        a: integer = b_ar(arr[0,1_2, a::"string"], func(lst[foo(a,1,2.2)]), a==b);
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(b_ar, [ArrayCell(arr, [IntegerLit(0), IntegerLit(12), BinExpr(::, Id(a), StringLit(string))]), FuncCall(func, [ArrayCell(lst, [FuncCall(foo, [Id(a), IntegerLit(1), FloatLit(2.2)])])]), BinExpr(==, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_expr(self):
        """Simple mathematic expr"""
        input = """
        a:integer = 1+2+3+4-5-6-7+8+9;
        b:float = 1.1*2.2/3.3*.e1 % 0.02e+2;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)), IntegerLit(6)), IntegerLit(7)), IntegerLit(8)), IntegerLit(9)))
	VarDecl(b, FloatType, BinExpr(%, BinExpr(*, BinExpr(/, BinExpr(*, FloatLit(1.1), FloatLit(2.2)), FloatLit(3.3)), FloatLit(0.0)), FloatLit(2.0)))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    
    def test_expr1(self):
        """Simple logic expr"""
        input = """
        a:boolean = ((a<b)>=c)>=(d==e);
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(>=, BinExpr(>=, BinExpr(<, Id(a), Id(b)), Id(c)), BinExpr(==, Id(d), Id(e))))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    
    def test_expr2(self):
        """Simple logic expr"""
        input = """
        a:boolean = a && b || true && (a>=b || (c==d));
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(a), Id(b)), BooleanLit(True)), BinExpr(>=, Id(a), BinExpr(||, Id(b), BinExpr(==, Id(c), Id(d))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_expr3(self):
        """Simple unary expr"""
        input = """
        a:boolean = !a;
        b:boolean = !false;
        b:boolean = !arr[true];
        """
        expect = """Program([
	VarDecl(a, BooleanType, UnExpr(!, Id(a)))
	VarDecl(b, BooleanType, UnExpr(!, BooleanLit(False)))
	VarDecl(b, BooleanType, UnExpr(!, ArrayCell(arr, [BooleanLit(True)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_expr4a(self):
        """Test expression parsing for other types of operands"""
        input = """
        a:array[0] of float = {{1,2}, {arr[0,1], .e-2}, {{"s1"}, {"\\"s2\\""}}}; /*test arr lit*/
        b:string = "string1"::arra[2,foo(arr[1]),arr[1_2]];
        c:auto = ((a==arr[0])!=(c<(true<=e)))>(1.2>=foo(foo(9)));
        """
        expect = """Program([
	VarDecl(a, ArrayType([0], FloatType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), FloatLit(0.0)]), ArrayLit([ArrayLit([StringLit(s1)]), ArrayLit([StringLit(\\"s2\\")])])]))
	VarDecl(b, StringType, BinExpr(::, StringLit(string1), ArrayCell(arra, [IntegerLit(2), FuncCall(foo, [ArrayCell(arr, [IntegerLit(1)])]), ArrayCell(arr, [IntegerLit(12)])])))
	VarDecl(c, AutoType, BinExpr(>, BinExpr(!=, BinExpr(==, Id(a), ArrayCell(arr, [IntegerLit(0)])), BinExpr(<, Id(c), BinExpr(<=, BooleanLit(True), Id(e)))), BinExpr(>=, FloatLit(1.2), FuncCall(foo, [FuncCall(foo, [IntegerLit(9)])]))))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_expr4b(self):
        """Test expression parsing for other types of operands"""
        input = """
        d:boolean = true&&false||arr[0];
        e:auto = 1-foo(2*a)+arr[b/2]%3;
        f:boolean = !bar();
        g:integer = arr[-2];
        """
        expect = """Program([
	VarDecl(d, BooleanType, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), ArrayCell(arr, [IntegerLit(0)])))
	VarDecl(e, AutoType, BinExpr(+, BinExpr(-, IntegerLit(1), FuncCall(foo, [BinExpr(*, IntegerLit(2), Id(a))])), BinExpr(%, ArrayCell(arr, [BinExpr(/, Id(b), IntegerLit(2))]), IntegerLit(3))))
	VarDecl(f, BooleanType, UnExpr(!, FuncCall(bar, [])))
	VarDecl(g, IntegerType, ArrayCell(arr, [UnExpr(-, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    
    def test_expr5(self):
        """Test sub expressions with id and lit"""
        input = """
        a:auto = (a+b);
        b:integer = 2*(1_2 - __9id);
        c:float = 2*(3-a+(b-c)/2)%3;
        d:auto = 2/(2+(2*(2%(2/(0)))));
        """
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(+, Id(a), Id(b)))
	VarDecl(b, IntegerType, BinExpr(*, IntegerLit(2), BinExpr(-, IntegerLit(12), Id(__9id))))
	VarDecl(c, FloatType, BinExpr(%, BinExpr(*, IntegerLit(2), BinExpr(+, BinExpr(-, IntegerLit(3), Id(a)), BinExpr(/, BinExpr(-, Id(b), Id(c)), IntegerLit(2)))), IntegerLit(3)))
	VarDecl(d, AutoType, BinExpr(/, IntegerLit(2), BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(2), BinExpr(%, IntegerLit(2), BinExpr(/, IntegerLit(2), IntegerLit(0)))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_expr6(self):
        """Test sub expressions with other operands"""
        input = """
        a:auto = (arr[0] + foo(3));
        b:integer = (arr[1,2] + arr[0,2_0]) / (foo(1) + bar());
        """
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(+, ArrayCell(arr, [IntegerLit(0)]), FuncCall(foo, [IntegerLit(3)])))
	VarDecl(b, IntegerType, BinExpr(/, BinExpr(+, ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]), ArrayCell(arr, [IntegerLit(0), IntegerLit(20)])), BinExpr(+, FuncCall(foo, [IntegerLit(1)]), FuncCall(bar, []))))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    
    def test_expr7(self):
        """Test sub expressions with other operands"""
        input = """
        c:float = arr[2/(2+(2*(2%(2/(0)))))];
        d:auto = func(2/(2+(2*(2%(2/(0))))));
        """
        expect = """Program([
	VarDecl(c, FloatType, ArrayCell(arr, [BinExpr(/, IntegerLit(2), BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(2), BinExpr(%, IntegerLit(2), BinExpr(/, IntegerLit(2), IntegerLit(0))))))]))
	VarDecl(d, AutoType, FuncCall(func, [BinExpr(/, IntegerLit(2), BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(2), BinExpr(%, IntegerLit(2), BinExpr(/, IntegerLit(2), IntegerLit(0))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_expr8(self):
        """Test non associative operators"""
        input = """
        main:function void(){
            a:integer = a==b;
            b:boolean = a==(b==c);
            c:boolean = (a==b)==c;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(==, Id(a), Id(b))), VarDecl(b, BooleanType, BinExpr(==, Id(a), BinExpr(==, Id(b), Id(c)))), VarDecl(c, BooleanType, BinExpr(==, BinExpr(==, Id(a), Id(b)), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_expr_precedence(self):
        input = """
        a:integer = a*2+1 + c/3 - false%true;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, BinExpr(+, BinExpr(*, Id(a), IntegerLit(2)), IntegerLit(1)), BinExpr(/, Id(c), IntegerLit(3))), BinExpr(%, BooleanLit(False), BooleanLit(True))))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_expr_precedence1(self):
        input = """
        a:boolean = a&&b < c||d;
        b:boolean = a&& b<c ||d; 
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(<, BinExpr(&&, Id(a), Id(b)), BinExpr(||, Id(c), Id(d))))
	VarDecl(b, BooleanType, BinExpr(<, BinExpr(&&, Id(a), Id(b)), BinExpr(||, Id(c), Id(d))))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_expr_precedence2(self):
        input = """
        a:boolean = a==c&&d;
        b:boolean = (a==c)&&d;
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(==, Id(a), BinExpr(&&, Id(c), Id(d))))
	VarDecl(b, BooleanType, BinExpr(&&, BinExpr(==, Id(a), Id(c)), Id(d)))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_expr_precedence3(self):
        input = """
        a:boolean = a==c&&d;
        b:boolean = (a==c)&&d;
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(==, Id(a), BinExpr(&&, Id(c), Id(d))))
	VarDecl(b, BooleanType, BinExpr(&&, BinExpr(==, Id(a), Id(c)), Id(d)))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_expr_precedence4(self):
        input = """
        a:string = a::b<=c&&d+e*f || !false;
        b:auto = -1/2-3||4!=5::6;
        """
        expect = """Program([
	VarDecl(a, StringType, BinExpr(::, Id(a), BinExpr(<=, Id(b), BinExpr(||, BinExpr(&&, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f)))), UnExpr(!, BooleanLit(False))))))
	VarDecl(b, AutoType, BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(-, BinExpr(/, UnExpr(-, IntegerLit(1)), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)), IntegerLit(6)))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_expr_precedence5(self):
        input = """
        a:auto = !-2;
        b:auto = !(-2);
        c:auto = -(!2);
        """
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(!, UnExpr(-, IntegerLit(2))))
	VarDecl(b, AutoType, UnExpr(!, UnExpr(-, IntegerLit(2))))
	VarDecl(c, AutoType, UnExpr(-, UnExpr(!, IntegerLit(2))))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_expr_precedence6(self):
        input = """
        a:boolean = !!!!!!true;
        b:boolean = ----2;
        c:string = !!-2;
        d:string = --(!2);
        """
        expect = """Program([
	VarDecl(a, BooleanType, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, BooleanLit(True))))))))
	VarDecl(b, BooleanType, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(2))))))
	VarDecl(c, StringType, UnExpr(!, UnExpr(!, UnExpr(-, IntegerLit(2)))))
	VarDecl(d, StringType, UnExpr(-, UnExpr(-, UnExpr(!, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_expr_precedence7(self):
        input = """
        a:auto = !(-(!2));
        a:auto = -(-(!2));
        """
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(!, UnExpr(-, UnExpr(!, IntegerLit(2)))))
	VarDecl(a, AutoType, UnExpr(-, UnExpr(-, UnExpr(!, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_expr_precedence8(self):
        input = """
        a:auto = !-(!2);
        b:auto = -(!(-2));
        """
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(!, UnExpr(-, UnExpr(!, IntegerLit(2)))))
	VarDecl(b, AutoType, UnExpr(-, UnExpr(!, UnExpr(-, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_expr_assoc(self):
        input = """
        a:integer = 1+2+3+4+5;
        b:integer = 1-2-3-4-5;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)))
	VarDecl(b, IntegerType, BinExpr(-, BinExpr(-, BinExpr(-, BinExpr(-, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_expr_assoc1(self):
        input = """
        a:integer = 1*2*3*4*5;
        b:integer = 1/2/3/4/5;
        c:float = 1%2%3%4%5;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(*, BinExpr(*, BinExpr(*, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)))
	VarDecl(b, IntegerType, BinExpr(/, BinExpr(/, BinExpr(/, BinExpr(/, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)))
	VarDecl(c, FloatType, BinExpr(%, BinExpr(%, BinExpr(%, BinExpr(%, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_expr_assoc2(self):
        input = """
        a:boolean = 1&&2&&3&&4&&5;
        b:integer = 1||2||3||4||5;
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(&&, BinExpr(&&, BinExpr(&&, BinExpr(&&, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)))
	VarDecl(b, IntegerType, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(||, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_stmt(self):
        input = """
        main : function void () {
            a = _09 + b - (2%3);
            arr[0, 1_2] = .e-23;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, Id(_09), Id(b)), BinExpr(%, IntegerLit(2), IntegerLit(3)))), AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(12)]), FloatLit(0.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_stmt1(self):
        input = """
        main : function void () {
            a = b;
            __a = ___;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(__a), Id(___))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    
    def test_stmt2(self):
        input = """
        main : function void () {
            int_var = 1_2 * (.e-3 + a)/b % 2;
            bool_var = a > b&&!c;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(int_var), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(12), BinExpr(+, FloatLit(0.0), Id(a))), Id(b)), IntegerLit(2))), AssignStmt(Id(bool_var), BinExpr(>, Id(a), BinExpr(&&, Id(b), UnExpr(!, Id(c)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_stmt3(self):
        input = """
        main : function void () {
            ret = foo(1*2/(3-a));
            idx = lst[1*2+foo(a)];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(ret), FuncCall(foo, [BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(-, IntegerLit(3), Id(a)))])), AssignStmt(Id(idx), ArrayCell(lst, [BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), FuncCall(foo, [Id(a)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_stmt4(self):
        input = """
        main : function void () {
            ret = foo(1*2/(3-a));
            idx = lst[1*2+foo(a)];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(ret), FuncCall(foo, [BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(-, IntegerLit(3), Id(a)))])), AssignStmt(Id(idx), ArrayCell(lst, [BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), FuncCall(foo, [Id(a)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_stmt5(self):
        input = """
        main : function void () {
            mret = foo(1, "str", foo(3,4,5), {1,2});
            eret = foo();
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(mret), FuncCall(foo, [IntegerLit(1), StringLit(str), FuncCall(foo, [IntegerLit(3), IntegerLit(4), IntegerLit(5)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])), AssignStmt(Id(eret), FuncCall(foo, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    
    def test_stmt6(self):
        input = """
        main : function void () {
            midx = lst[id[1,2], id[3,4], 5];
            mmidx = lst[lv1[1,2], lv1[3, lv2[4, lv3[5]]]];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(midx), ArrayCell(lst, [ArrayCell(id, [IntegerLit(1), IntegerLit(2)]), ArrayCell(id, [IntegerLit(3), IntegerLit(4)]), IntegerLit(5)])), AssignStmt(Id(mmidx), ArrayCell(lst, [ArrayCell(lv1, [IntegerLit(1), IntegerLit(2)]), ArrayCell(lv1, [IntegerLit(3), ArrayCell(lv2, [IntegerLit(4), ArrayCell(lv3, [IntegerLit(5)])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    
    def test_stmt7(self):
        input = """
        main : function void () {
            if (a) a=b;
            if (b) {a=b;}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), AssignStmt(Id(a), Id(b))), IfStmt(Id(b), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_stmt8(self):
        input = """
        main : function void () {
            if (a) a=b; else
            if (b) {a=b;} else {}
            if (b) {} else {}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), AssignStmt(Id(a), Id(b)), IfStmt(Id(b), BlockStmt([AssignStmt(Id(a), Id(b))]), BlockStmt([]))), IfStmt(Id(b), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_stmt9(self):
        input = r"""
        main : function void () {
            if (a*b<c&&!true%2) a=foo(arr[a]);
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, BinExpr(*, Id(a), Id(b)), BinExpr(&&, Id(c), BinExpr(%, UnExpr(!, BooleanLit(True)), IntegerLit(2)))), AssignStmt(Id(a), FuncCall(foo, [ArrayCell(arr, [Id(a)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    
    def test_stmt10(self):
        input = r"""
        main : function void () {
            if (arr[0]) {
                a=foo(arr[a]);
                return a;
            }
            else continue;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(ArrayCell(arr, [IntegerLit(0)]), BlockStmt([AssignStmt(Id(a), FuncCall(foo, [ArrayCell(arr, [Id(a)])])), ReturnStmt(Id(a))]), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_program22(self):
        input = """main: function void() {}
            foo: function string(n: string) {
                a = "abc" + "abc";  
                for (i = 1, i <= 100, i+1) write(testcase);
                a = {a + foo(3),-b,c[0]} + power(-a);
                if (!true && (true && !false + -abc)) return a;
                return {a,-b,b % c};
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, StringType, [Param(n, StringType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, StringLit(abc), StringLit(abc))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(write, Id(testcase))), AssignStmt(Id(a), BinExpr(+, ArrayLit([BinExpr(+, Id(a), FuncCall(foo, [IntegerLit(3)])), UnExpr(-, Id(b)), ArrayCell(c, [IntegerLit(0)])]), FuncCall(power, [UnExpr(-, Id(a))]))), IfStmt(BinExpr(&&, UnExpr(!, BooleanLit(True)), BinExpr(&&, BooleanLit(True), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, Id(abc))))), ReturnStmt(Id(a))), ReturnStmt(ArrayLit([Id(a), UnExpr(-, Id(b)), BinExpr(%, Id(b), Id(c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    
    def test_stmt11(self):
        input = r"""
        main : function void () {
            if (arr[0]) {
                a=foo(arr[a]);
                return a;
            }
            else {
                a=b;
                b=!false;
                continue;
            }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(ArrayCell(arr, [IntegerLit(0)]), BlockStmt([AssignStmt(Id(a), FuncCall(foo, [ArrayCell(arr, [Id(a)])])), ReturnStmt(Id(a))]), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), UnExpr(!, BooleanLit(False))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    
    def test_stmt12(self):
        input = r"""
        main : function void () {
            if (1) {
                if (2)
                    if (3)
                        if (4) {}
                        else return;
            }
            else {
                if (2)
                    if (3)
                    {
                        a=b==c;
                        continue;
                    }
            }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(IntegerLit(1), BlockStmt([IfStmt(IntegerLit(2), IfStmt(IntegerLit(3), IfStmt(IntegerLit(4), BlockStmt([]), ReturnStmt())))]), BlockStmt([IfStmt(IntegerLit(2), IfStmt(IntegerLit(3), BlockStmt([AssignStmt(Id(a), BinExpr(==, Id(b), Id(c))), ContinueStmt()])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_stmt12b(self):
        input = r"""
        main : function void () {
            for (a=1, 1-2, 2<=2) return;
            for (a=1, 1-2, 2<=2) {}
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(<=, IntegerLit(2), IntegerLit(2)), ReturnStmt()), ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(<=, IntegerLit(2), IntegerLit(2)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    def test_stmt13(self):
        input = r"""
        main : function void () {
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
            {
                b=c;
                continue;
                return;
                return 2*2%2/2;
            }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), BlockStmt([AssignStmt(Id(b), Id(c)), ContinueStmt(), ReturnStmt(), ReturnStmt(BinExpr(/, BinExpr(%, BinExpr(*, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_stmt14(self):
        input = r"""
        main : function void () {
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
                a=2;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), AssignStmt(Id(a), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_stmt15(self):
        input = r"""
        main : function void () {
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
                a=2;
            for (ar[foo(false)] = b*a, 1-2<3*!true, a) 
                a=2;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), AssignStmt(Id(a), IntegerLit(2))), ForStmt(AssignStmt(ArrayCell(ar, [FuncCall(foo, [BooleanLit(False)])]), BinExpr(*, Id(b), Id(a))), BinExpr(<, BinExpr(-, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), UnExpr(!, BooleanLit(True)))), Id(a), AssignStmt(Id(a), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    def test_stmt16(self):
        input = r"""
        main : function void () {
            for (a=1, a!=2, a+1*b) 
                for (b=b, b, b) 
                    for (c=c, c, c) 
                        for (d=d, d, d) continue;   
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(!=, Id(a), IntegerLit(2)), BinExpr(+, Id(a), BinExpr(*, IntegerLit(1), Id(b))), ForStmt(AssignStmt(Id(b), Id(b)), Id(b), Id(b), ForStmt(AssignStmt(Id(c), Id(c)), Id(c), Id(c), ForStmt(AssignStmt(Id(d), Id(d)), Id(d), Id(d), ContinueStmt()))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_stmt16a(self):
        input = """
        main : function void () {
            do{
            
            }
            while (a);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test_stmt17(self):
        input = """
        main : function void () {
            do{
                a=b;
                b = 1*2/3 + 2%22 <1;
                break;
            }
            while ( a==(1<-c) );
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), BinExpr(<, IntegerLit(1), UnExpr(-, Id(c)))), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), BinExpr(<, BinExpr(+, BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(%, IntegerLit(2), IntegerLit(22))), IntegerLit(1))), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test_stmt17a(self):
        input = """
        main : function void () {
            do{
                do{
                    do{
                        return a!=!c;
                    }while (3);
                }
                while (2);
            }
            while (1);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(IntegerLit(1), BlockStmt([DoWhileStmt(IntegerLit(2), BlockStmt([DoWhileStmt(IntegerLit(3), BlockStmt([ReturnStmt(BinExpr(!=, Id(a), UnExpr(!, Id(c))))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_stmt18(self):
        input = """
        main : function void () {
            for (a=2, a==b, a+b*2%3)
                continue;
            for (a=2, a==b, a+b*2%3)
            {
                c: integer = true;
                b = (b+1)/2 || c;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), ContinueStmt()), ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), BlockStmt([VarDecl(c, IntegerType, BooleanLit(True)), AssignStmt(Id(b), BinExpr(||, BinExpr(/, BinExpr(+, Id(b), IntegerLit(1)), IntegerLit(2)), Id(c)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_stmt19(self):
        input = """
        main : function void () {
            for (a=2, a==b, a+b*2%3)
                continue;
            for (arr[2_2]=2E-3, arr[2], a+b*2%3)
            {
                c: integer = true;
                b = (b+1)/2 || c;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), ContinueStmt()), ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(22)]), FloatLit(0.002)), ArrayCell(arr, [IntegerLit(2)]), BinExpr(+, Id(a), BinExpr(%, BinExpr(*, Id(b), IntegerLit(2)), IntegerLit(3))), BlockStmt([VarDecl(c, IntegerType, BooleanLit(True)), AssignStmt(Id(b), BinExpr(||, BinExpr(/, BinExpr(+, Id(b), IntegerLit(1)), IntegerLit(2)), Id(c)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_stmt20(self):
        input = """
        main : function void () {
            for (a=a, a||b, !a+b&&2%3)
                for (arr[0]=1_2, arr[1], !true)
                {
                    a = b;
                    for (_0id=1, ("sub"+"\\"expr\\""), a!=false)
                        return;
                }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), Id(a)), BinExpr(||, Id(a), Id(b)), BinExpr(&&, BinExpr(+, UnExpr(!, Id(a)), Id(b)), BinExpr(%, IntegerLit(2), IntegerLit(3))), ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(0)]), IntegerLit(12)), ArrayCell(arr, [IntegerLit(1)]), UnExpr(!, BooleanLit(True)), BlockStmt([AssignStmt(Id(a), Id(b)), ForStmt(AssignStmt(Id(_0id), IntegerLit(1)), BinExpr(+, StringLit(sub), StringLit(\\"expr\\")), BinExpr(!=, Id(a), BooleanLit(False)), ReturnStmt())])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_call_stmt(self):
        input = """
        main : function void () {
            foo(a*foo("string"/(a-arr[foo()])%2), b, 2_2.E-2);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, Id(a), FuncCall(foo, [BinExpr(%, BinExpr(/, StringLit(string), BinExpr(-, Id(a), ArrayCell(arr, [FuncCall(foo, [])]))), IntegerLit(2))])), Id(b), FloatLit(0.22))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_complex_exp(self):
        input = r"""
        a:auto = -2 / !false :: b<=c || (true!=fal) % 3;
        """
        expect = r"""Program([
	VarDecl(a, AutoType, BinExpr(::, BinExpr(/, UnExpr(-, IntegerLit(2)), UnExpr(!, BooleanLit(False))), BinExpr(<=, Id(b), BinExpr(||, Id(c), BinExpr(%, BinExpr(!=, BooleanLit(True), Id(fal)), IntegerLit(3))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
       
    def test_complex_exp1(self):
        input = r"""
        a:auto = -2 / (!false :: b<=-c) || (foo()+arr[a]) % -3-2;
        """
        expect = r"""Program([
	VarDecl(a, AutoType, BinExpr(||, BinExpr(/, UnExpr(-, IntegerLit(2)), BinExpr(::, UnExpr(!, BooleanLit(False)), BinExpr(<=, Id(b), UnExpr(-, Id(c))))), BinExpr(-, BinExpr(%, BinExpr(+, FuncCall(foo, []), ArrayCell(arr, [Id(a)])), UnExpr(-, IntegerLit(3))), IntegerLit(2))))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_complex_exp1(self):
        input = r"""
        a:integer = 2--2;
        b:integer = 2-2-2-2--2;
        c:integer = ----2;
        d:integer = 1---2;
        """
        expect = r"""Program([
	VarDecl(a, IntegerType, BinExpr(-, IntegerLit(2), UnExpr(-, IntegerLit(2))))
	VarDecl(b, IntegerType, BinExpr(-, BinExpr(-, BinExpr(-, BinExpr(-, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), IntegerLit(2)), UnExpr(-, IntegerLit(2))))
	VarDecl(c, IntegerType, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(2))))))
	VarDecl(d, IntegerType, BinExpr(-, IntegerLit(1), UnExpr(-, UnExpr(-, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_prog(self):
        input = r"""
        main: function void(){
            a: integer = 0; 
            {
                inner = a;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), BlockStmt([AssignStmt(Id(inner), Id(a))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_prog1(self):
        input = r"""
        all: auto;

        foo: function auto (out arr: array[4] of string, incr: integer){
            for (i=0, i<=4, i+1)
                arr[i] = (arr[i]+incr)*(4&&a)%2;
        }

        main: function void(){
            a: integer = 0;
            b: array[1_2] of float = {1.1, .E-3, 1_1_2.002E+2};
            return foo(b, a);
        }
        """
        expect = """Program([
	VarDecl(all, AutoType)
	FuncDecl(foo, AutoType, [OutParam(arr, ArrayType([4], StringType)), Param(incr, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(%, BinExpr(*, BinExpr(+, ArrayCell(arr, [Id(i)]), Id(incr)), BinExpr(&&, IntegerLit(4), Id(a))), IntegerLit(2))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, ArrayType([12], FloatType), ArrayLit([FloatLit(1.1), FloatLit(0.0), FloatLit(11200.2)])), ReturnStmt(FuncCall(foo, [Id(b), Id(a)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_prog2(self):
        input = r"""
        count: integer = 0;
        loop_cond: boolean = true; 
        main: function void(){
            while(loop_cond)
                if (count % 12 == 0) continue;
            do{
                // nullable
            } while (count <= true || false);
            return arr[main(foo(arr[main()]))];
        }
        """
        expect = """Program([
	VarDecl(count, IntegerType, IntegerLit(0))
	VarDecl(loop_cond, BooleanType, BooleanLit(True))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(Id(loop_cond), IfStmt(BinExpr(==, BinExpr(%, Id(count), IntegerLit(12)), IntegerLit(0)), ContinueStmt())), DoWhileStmt(BinExpr(<=, Id(count), BinExpr(||, BooleanLit(True), BooleanLit(False))), BlockStmt([])), ReturnStmt(ArrayCell(arr, [FuncCall(main, [FuncCall(foo, [ArrayCell(arr, [FuncCall(main, [])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_prog3(self):
        input = r"""
        count: integer = 0;
        loop_cond: boolean = true; 
        main: function void(){
            while(loop_cond)
                if (count % 12 == 0)
                    do{
                        for (i=0, i<=4, i+1){
                            if (i%2==0)
                                arr[i] = (arr[i]+incr)*(4&&a)%2;
                            else
                                {
                                    foo("string\"", _0id, "string\t\"");
                                }
                        }
                    } while (count <= true || false);
            return arr[main(foo(arr[main()]))];
        }
        """
        expect = r"""Program([
	VarDecl(count, IntegerType, IntegerLit(0))
	VarDecl(loop_cond, BooleanType, BooleanLit(True))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(Id(loop_cond), IfStmt(BinExpr(==, BinExpr(%, Id(count), IntegerLit(12)), IntegerLit(0)), DoWhileStmt(BinExpr(<=, Id(count), BinExpr(||, BooleanLit(True), BooleanLit(False))), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(%, BinExpr(*, BinExpr(+, ArrayCell(arr, [Id(i)]), Id(incr)), BinExpr(&&, IntegerLit(4), Id(a))), IntegerLit(2))), BlockStmt([CallStmt(foo, StringLit(string\"), Id(_0id), StringLit(string\t\"))]))]))])))), ReturnStmt(ArrayCell(arr, [FuncCall(main, [FuncCall(foo, [ArrayCell(arr, [FuncCall(main, [])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_prog4(self):
        input = r"""
        // Variable declarations
        a: integer = 1_2_3_4;
        b: float = 1_2_3.0011E+1;
        c: string = "true\"false\n\t\"True\\False";
        d: array[1_2] of boolean = {true, "faLse", a::b, c};
        __01, id_09, True : auto = 1, {1,2,3}, "str\"in\'g";
        //*function decls*//
        
        func: function auto (inherit a:integer, out b: float, inherit out _0c: array[0] of string){
            for (d[foo(arr[0])] = (d[0]*a)/b||c%(!false), "string" != "\"\"", arr[foo(a&&b||c)] )
                foo(arr[0]);
            break;
        }

        /*more function*///*/
        foo: function array[0] of boolean(){
            while (arr[0] <= foo(arr[1_2, func(1.2e+3)]))
                if (count(arr) % (a||b&&c/d) == 0) continue;
                else 
                    if (a+b%c(true&&bar(arr[foo(3::4)]&&(!false+(-2))))) {
                        arr[1, foo(2), arr[9], 1_2, .e-12] = arr[1, foo(2), arr[9], 1_2, .e-12];
                    }
                    else return func("string\t\"inner\b\f\"\nanother \\ line");
                foo();
        }
        
        main: function void(){
            do{
                for (foo = arr[arr[1,2]], (a&&b+12-!2)/12, 1)
                    if (a+b%c(true&&bar(arr[foo(3::4)]&&(!false+(-2))))) continue;
                    else break;
                    while (count(arr) % (a||b&&c/d) == 0){
                        //nullable
                    }
            }while(a+b%c(true&&bar(arr[foo(3::4)]&&(!false+(-2)))));
            return;
        }
        """
        expect = r"""Program([
	VarDecl(a, IntegerType, IntegerLit(1234))
	VarDecl(b, FloatType, FloatLit(1230.011))
	VarDecl(c, StringType, StringLit(true\"false\n\t\"True\\False))
	VarDecl(d, ArrayType([12], BooleanType), ArrayLit([BooleanLit(True), StringLit(faLse), BinExpr(::, Id(a), Id(b)), Id(c)]))
	VarDecl(__01, AutoType, IntegerLit(1))
	VarDecl(id_09, AutoType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(True, AutoType, StringLit(str\"in\'g))
	FuncDecl(func, AutoType, [InheritParam(a, IntegerType), OutParam(b, FloatType), InheritOutParam(_0c, ArrayType([0], StringType))], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(d, [FuncCall(foo, [ArrayCell(arr, [IntegerLit(0)])])]), BinExpr(||, BinExpr(/, BinExpr(*, ArrayCell(d, [IntegerLit(0)]), Id(a)), Id(b)), BinExpr(%, Id(c), UnExpr(!, BooleanLit(False))))), BinExpr(!=, StringLit(string), StringLit(\"\")), ArrayCell(arr, [FuncCall(foo, [BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c))])]), CallStmt(foo, ArrayCell(arr, [IntegerLit(0)]))), BreakStmt()]))
	FuncDecl(foo, ArrayType([0], BooleanType), [], None, BlockStmt([WhileStmt(BinExpr(<=, ArrayCell(arr, [IntegerLit(0)]), FuncCall(foo, [ArrayCell(arr, [IntegerLit(12), FuncCall(func, [FloatLit(1200.0)])])])), IfStmt(BinExpr(==, BinExpr(%, FuncCall(count, [Id(arr)]), BinExpr(&&, BinExpr(||, Id(a), Id(b)), BinExpr(/, Id(c), Id(d)))), IntegerLit(0)), ContinueStmt(), IfStmt(BinExpr(+, Id(a), BinExpr(%, Id(b), FuncCall(c, [BinExpr(&&, BooleanLit(True), FuncCall(bar, [BinExpr(&&, ArrayCell(arr, [FuncCall(foo, [BinExpr(::, IntegerLit(3), IntegerLit(4))])]), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, IntegerLit(2))))]))]))), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(1), FuncCall(foo, [IntegerLit(2)]), ArrayCell(arr, [IntegerLit(9)]), IntegerLit(12), FloatLit(0.0)]), ArrayCell(arr, [IntegerLit(1), FuncCall(foo, [IntegerLit(2)]), ArrayCell(arr, [IntegerLit(9)]), IntegerLit(12), FloatLit(0.0)]))]), ReturnStmt(FuncCall(func, [StringLit(string\t\"inner\b\f\"\nanother \\ line)]))))), CallStmt(foo, )]))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, Id(a), BinExpr(%, Id(b), FuncCall(c, [BinExpr(&&, BooleanLit(True), FuncCall(bar, [BinExpr(&&, ArrayCell(arr, [FuncCall(foo, [BinExpr(::, IntegerLit(3), IntegerLit(4))])]), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, IntegerLit(2))))]))]))), BlockStmt([ForStmt(AssignStmt(Id(foo), ArrayCell(arr, [ArrayCell(arr, [IntegerLit(1), IntegerLit(2)])])), BinExpr(/, BinExpr(&&, Id(a), BinExpr(-, BinExpr(+, Id(b), IntegerLit(12)), UnExpr(!, IntegerLit(2)))), IntegerLit(12)), IntegerLit(1), IfStmt(BinExpr(+, Id(a), BinExpr(%, Id(b), FuncCall(c, [BinExpr(&&, BooleanLit(True), FuncCall(bar, [BinExpr(&&, ArrayCell(arr, [FuncCall(foo, [BinExpr(::, IntegerLit(3), IntegerLit(4))])]), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, IntegerLit(2))))]))]))), ContinueStmt(), BreakStmt())), WhileStmt(BinExpr(==, BinExpr(%, FuncCall(count, [Id(arr)]), BinExpr(&&, BinExpr(||, Id(a), Id(b)), BinExpr(/, Id(c), Id(d)))), IntegerLit(0)), BlockStmt([]))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_multi_full_vardecl(self):
        input = """
        x, y: integer = 1*2, 2+3;
        a: string = "abc" :: "def";
        d: integer = a[1+2, 1*5];
        c: string = a(1, f("abc"));
        """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(d, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
	VarDecl(c, StringType, FuncCall(a, [IntegerLit(1), FuncCall(f, [StringLit(abc)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_ifstmt(self):
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello";
        else a[0] = "in else";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(in else)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_dowhile(self):
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
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(c, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(c), StringLit()), BlockStmt([CallStmt(readString, StringLit(abc)), AssignStmt(Id(c), BinExpr(::, Id(c), StringLit(abc))), CallStmt(printString, Id(c))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_funcdecl_full(self):
        input = """
    testfunc: function void (inherit out a: array[1] of boolean) {
        if(a[1, 2] == "true")
            super(printInteger(a[1*2, 3+4]), x%2);
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([1], BooleanType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), StringLit(true)), CallStmt(super, FuncCall(printInteger, [ArrayCell(a, [BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(3), IntegerLit(4))])]), BinExpr(%, Id(x), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_prog5(self):
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
        expect = """Program([
	FuncDecl(foo, FloatType, [], None, BlockStmt([ReturnStmt(FloatLit(1.233233e-17))]))
	FuncDecl(bar, FloatType, [], None, BlockStmt([ReturnStmt(FuncCall(foo, []))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, BinExpr(%, IntegerLit(23), IntegerLit(2)), IntegerLit(23)), BinExpr(%, IntegerLit(332), IntegerLit(90)))), VarDecl(z, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False))), VarDecl(b, FloatType, BinExpr(-, BinExpr(-, FloatLit(2.323232e+28), FloatLit(2.322e+26)), BinExpr(*, FuncCall(foo, []), FuncCall(bar, [])))), CallStmt(printInteger, Id(a)), CallStmt(writeFloat, Id(b)), IfStmt(BinExpr(==, Id(z), BooleanLit(True)), BlockStmt([CallStmt(print, StringLit(TRUE))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_prog6(self):
        input = r"""
        return_string: function string() {
            return "hello world";
        }
        main:function void(){
            a: array [2] of string = {foo(), foo()};
            i: integer = 0;
            while(i<2){
                print(a[i]);
                if(i == 1) {
                    i = 0;
                    break;
                }
            i = i+1;
            }
        }
        """
        expect = """Program([
	FuncDecl(return_string, StringType, [], None, BlockStmt([ReturnStmt(StringLit(hello world))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], StringType), ArrayLit([FuncCall(foo, []), FuncCall(foo, [])])), VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(2)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i)])), IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(0)), BreakStmt()])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_prog7(self):
        input = r"""
        is_prime: function boolean (n: integer, out a:boolean) inherit main
        {
            if (n <= 1) return false;
            else if (n <=3) return true;
            
            if ((n % 2 == 0) || (n % 3 == 0)) return false;
            i: integer = 5;
            while (i * i <= n){
                if ((n % i == 0) || (n % (i + 2) == 0)){
                    return false;
                }
                i = i + 6;
            }
            return true;
        }
        """
        expect = """Program([
	FuncDecl(is_prime, BooleanType, [Param(n, IntegerType), OutParam(a, BooleanType)], main, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), ReturnStmt(BooleanLit(False)), IfStmt(BinExpr(<=, Id(n), IntegerLit(3)), ReturnStmt(BooleanLit(True)))), IfStmt(BinExpr(||, BinExpr(==, BinExpr(%, Id(n), IntegerLit(2)), IntegerLit(0)), BinExpr(==, BinExpr(%, Id(n), IntegerLit(3)), IntegerLit(0))), ReturnStmt(BooleanLit(False))), VarDecl(i, IntegerType, IntegerLit(5)), WhileStmt(BinExpr(<=, BinExpr(*, Id(i), Id(i)), Id(n)), BlockStmt([IfStmt(BinExpr(||, BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BinExpr(==, BinExpr(%, Id(n), BinExpr(+, Id(i), IntegerLit(2))), IntegerLit(0))), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(6)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_prog8(self):
        input = r"""
        main: function void(){
            for (i = 0, i < 10, i+1){
                for(j = 0, j < 10, j+1){
                    while (i < j){
                        i = i + 1;
                        j = j - 1;
                        do{
                            n: integer = 3;
                            inc(n);
                        }
                        while (i < 5);
                    }
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, Id(i), Id(j)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1))), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([VarDecl(n, IntegerType, IntegerLit(3)), CallStmt(inc, Id(n))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_prog9(self):
        input = r"""
        main: function integer(){
            isBad: boolean = true;
            do{
                do{
                    do{
                        if (rand(1,200) == 69){
                            isBad = false;
                        }
                    }
                    while (isBad == true);
                }
                while (isBad == true);  
            }
            while (isBad == true);
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(isBad, BooleanType, BooleanLit(True)), DoWhileStmt(BinExpr(==, Id(isBad), BooleanLit(True)), BlockStmt([DoWhileStmt(BinExpr(==, Id(isBad), BooleanLit(True)), BlockStmt([DoWhileStmt(BinExpr(==, Id(isBad), BooleanLit(True)), BlockStmt([IfStmt(BinExpr(==, FuncCall(rand, [IntegerLit(1), IntegerLit(200)]), IntegerLit(69)), BlockStmt([AssignStmt(Id(isBad), BooleanLit(False))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_prog9a(self):
        """Simple program: int main() {} """
        input = """main: function void() {}
            foo: function string(n: string) {
                a = "abc" + "abc";  
                for (i = 1, i <= 100, i+1) write(testcase);
                a = {a + foo(3),-b,c[0]} + power(-a);
                if (!true && (true && !false + -abc)) return a;
                return {a,-b,b % c};
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, StringType, [Param(n, StringType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, StringLit(abc), StringLit(abc))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(write, Id(testcase))), AssignStmt(Id(a), BinExpr(+, ArrayLit([BinExpr(+, Id(a), FuncCall(foo, [IntegerLit(3)])), UnExpr(-, Id(b)), ArrayCell(c, [IntegerLit(0)])]), FuncCall(power, [UnExpr(-, Id(a))]))), IfStmt(BinExpr(&&, UnExpr(!, BooleanLit(True)), BinExpr(&&, BooleanLit(True), BinExpr(+, UnExpr(!, BooleanLit(False)), UnExpr(-, Id(abc))))), ReturnStmt(Id(a))), ReturnStmt(ArrayLit([Id(a), UnExpr(-, Id(b)), BinExpr(%, Id(b), Id(c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_prog10(self):
        input = r"""
        main: function integer(){
            isBad: boolean = true;
            while(isBad == true){
                print(a&&b||c);
                res: integer = rand(1,200);
                if (res == 69) break;
                else{
                    for(i = 1, i < 10, i+1){
                        print(a<=!c::i);
                    }
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(isBad, BooleanType, BooleanLit(True)), WhileStmt(BinExpr(==, Id(isBad), BooleanLit(True)), BlockStmt([CallStmt(print, BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c))), VarDecl(res, IntegerType, FuncCall(rand, [IntegerLit(1), IntegerLit(200)])), IfStmt(BinExpr(==, Id(res), IntegerLit(69)), BreakStmt(), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, BinExpr(::, BinExpr(<=, Id(a), UnExpr(!, Id(c))), Id(i)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_prog11(self):
        input = r"""
        a: integer = 1;
        b,c: float = 2.0, 10e-10;
        d,e,f: string = "str1", "str\n2\t3", "string\"Inner\'\n\"";
        g,h,i,j: boolean = true, false, false, true;
        k, l, m: auto;
        n, o: array[3] of integer = {1,2},{1,2};
        p: array[0] of string;
        """
        expect = r"""Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, FloatType, FloatLit(2.0))
	VarDecl(c, FloatType, FloatLit(1e-09))
	VarDecl(d, StringType, StringLit(str1))
	VarDecl(e, StringType, StringLit(str\n2\t3))
	VarDecl(f, StringType, StringLit(string\"Inner\'\n\"))
	VarDecl(g, BooleanType, BooleanLit(True))
	VarDecl(h, BooleanType, BooleanLit(False))
	VarDecl(i, BooleanType, BooleanLit(False))
	VarDecl(j, BooleanType, BooleanLit(True))
	VarDecl(k, AutoType)
	VarDecl(l, AutoType)
	VarDecl(m, AutoType)
	VarDecl(n, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(o, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(p, ArrayType([0], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_prog12(self):
        input = r"""
        main: function void() {
            for(i[1, 1+(foo("string"::"string")+i[0])] = 0, i <= 1, i+1)
                for(j = 0, j <= i, j+1) {
                    printFloat(j);
                }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(1), BinExpr(+, IntegerLit(1), BinExpr(+, FuncCall(foo, [BinExpr(::, StringLit(string), StringLit(string))]), ArrayCell(i, [IntegerLit(0)])))]), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<=, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printFloat, Id(j))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_prog13(self):
        input = r"""
        main: function void() {
            do {
                do {

                } while(true);
            } while (true);
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_prog14(self):
        input = r"""
        main: function void() {
            {
                {
                    {
                        a: string = "string";
                    }
                }
            }
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([VarDecl(a, StringType, StringLit(string))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_prog15(self):
        input = r"""
        main: function void() {
            a: boolean = (a == b) && ((f != r) || c != foo() && d) != var[0];
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BinExpr(!=, BinExpr(&&, BinExpr(==, Id(a), Id(b)), BinExpr(!=, BinExpr(||, BinExpr(!=, Id(f), Id(r)), Id(c)), BinExpr(&&, FuncCall(foo, []), Id(d)))), ArrayCell(var, [IntegerLit(0)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_prog16(self):
        input = r"""
        main: function void() {
                a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(::, StringLit(string), BinExpr(==, BinExpr(&&, Id(a), BinExpr(+, Id(c), BinExpr(*, IntegerLit(2), IntegerLit(3)))), BinExpr(||, BinExpr(-, Id(b), BinExpr(*, IntegerLit(2), UnExpr(!, UnExpr(-, ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))), Id(d)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_prog17(self):
        input = r"""
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        foo: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        bar: function void() {
            delta: integer = fact(3);
            inc(x,delta);
            printInteger(x);
        }
        """
        expect = r"""Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(foo, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(bar, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_prog18(self):
        input = r"""
        main: function void(out n: integer, inherit x: boolean) {
            if (!x) {
                foo(x);
                n = n+1;
                y: integer = 10;
                {
                    break;
                }
            } else {
                writeInt(y);
                continue;
                {
                    print(contin);
                }
            }
            return;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [OutParam(n, IntegerType), InheritParam(x, BooleanType)], None, BlockStmt([IfStmt(UnExpr(!, Id(x)), BlockStmt([CallStmt(foo, Id(x)), AssignStmt(Id(n), BinExpr(+, Id(n), IntegerLit(1))), VarDecl(y, IntegerType, IntegerLit(10)), BlockStmt([BreakStmt()])]), BlockStmt([CallStmt(writeInt, Id(y)), ContinueStmt(), BlockStmt([CallStmt(print, Id(contin))])])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_prog19(self):
        input = r"""
        main: function void(out n: integer, inherit x: boolean) inherit _f_o_12
        {
            a = "abc"::"cdf";
            a = a[0]::b[5];
            a = (a[0] + b[0]) :: abc;
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [OutParam(n, IntegerType), InheritParam(x, BooleanType)], _f_o_12, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(abc), StringLit(cdf))), AssignStmt(Id(a), BinExpr(::, ArrayCell(a, [IntegerLit(0)]), ArrayCell(b, [IntegerLit(5)]))), AssignStmt(Id(a), BinExpr(::, BinExpr(+, ArrayCell(a, [IntegerLit(0)]), ArrayCell(b, [IntegerLit(0)])), Id(abc)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test_prog20(self):
        input = r"""
        main: function void() {}
        foo: function integer(n: boolean) {
            a = a[a[0]+b[a[2] + c[0]]] + a[1] + a[5];  
            for (i = 1, i <= 100, i+1) write(testcase);
            continue;
            break;
            return a[b[2] + c[2]];
        }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, IntegerType, [Param(n, BooleanType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, ArrayCell(a, [BinExpr(+, ArrayCell(a, [IntegerLit(0)]), ArrayCell(b, [BinExpr(+, ArrayCell(a, [IntegerLit(2)]), ArrayCell(c, [IntegerLit(0)]))]))]), ArrayCell(a, [IntegerLit(1)])), ArrayCell(a, [IntegerLit(5)]))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(write, Id(testcase))), ContinueStmt(), BreakStmt(), ReturnStmt(ArrayCell(a, [BinExpr(+, ArrayCell(b, [IntegerLit(2)]), ArrayCell(c, [IntegerLit(2)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_prog21(self):
        input = r"""
        main: function void() {}
            foo: function integer(n: boolean) {
                a = a[a[0]+b[a[2] + c[0]]] + a[1] + a[5];  
                for (i = 1, i <= 100, i+1) write(testcase);
                a = {a,b,c[0]} + power(a);
                if (!true && (true && !false)) return a;
                return {a,b,c};
            }
        """
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, IntegerType, [Param(n, BooleanType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, ArrayCell(a, [BinExpr(+, ArrayCell(a, [IntegerLit(0)]), ArrayCell(b, [BinExpr(+, ArrayCell(a, [IntegerLit(2)]), ArrayCell(c, [IntegerLit(0)]))]))]), ArrayCell(a, [IntegerLit(1)])), ArrayCell(a, [IntegerLit(5)]))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(write, Id(testcase))), AssignStmt(Id(a), BinExpr(+, ArrayLit([Id(a), Id(b), ArrayCell(c, [IntegerLit(0)])]), FuncCall(power, [Id(a)]))), IfStmt(BinExpr(&&, UnExpr(!, BooleanLit(True)), BinExpr(&&, BooleanLit(True), UnExpr(!, BooleanLit(False)))), ReturnStmt(Id(a))), ReturnStmt(ArrayLit([Id(a), Id(b), Id(c)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))

    

    

    



    