
import unittest
from TestUtils import TestParser
 
 
class ParserSuite(unittest.TestCase):
    def testParser(self):
        input = """O,a,n,h: float = 1, 2, 1;"""
        expect = "Error on line 1 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 201))

        input = """main:  function void() {
            delta: integer = fact(a , 4);
            inc(1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

        input = """_abc, d16: auto = 15, 1.25;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

        input = """_123, Yz, Aaa: auto = -5 || "Watch movie please", 5::7, {56 && false, 1, 7};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

        input = """strArr: array[5] of string = "Oanh di hoc" == "Oanh luoi hoc qua";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

        input = """X_, _xy: floatint = "true", false;"""
        expect = "Error on line 1 col 9: floatint"
        self.assertTrue(TestParser.test(input, expect, 206))

        input = """
            _abc, d16: auto = 15, 1.25;;
            """
        expect = "Error on line 2 col 39: ;"
        self.assertTrue(TestParser.test(input, expect, 207))

        input = """main: function void() {
            // Day la mot dong binh luan
            /*
                Day la mot dong binh luan
            */
            // Day lai la mot dong binh luan
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

        input = """// hahhahaha
            y :: int;"""
        expect = "Error on line 2 col 14: ::"
        self.assertTrue(TestParser.test(input, expect, 209))

        input = """x: array[1 2] of void;"""
        expect = "Error on line 1 col 11: 2"
        self.assertTrue(TestParser.test(input, expect, 210))

        input = """main: function void() {
            a = 1-2-3;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

        input = """ranghoc: function int() a: integer;"""
        expect = "Error on line 1 col 18: int"
        self.assertTrue(TestParser.test(input, expect, 212))

        input = """X : integer = 65;
                    fact: function integer (n: integer){
	                if (n == 0) return 1;
	                else return n * fact(n-1);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

        input = """main: function void() {
            for(){
                a=10 + 1;
                if(a < 150) b=f[4];
            }
        }"""
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.test(input, expect, 214))

        input = """adoublefunction: function function() {}"""
        expect = "Error on line 1 col 26: function"
        self.assertTrue(TestParser.test(input, expect, 215))

        input = """integer: function boolean() {}"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 216))

        input = """fact: function integer (n: integer, inherit p: integer){
                    a,b,c,d: float;
                do{
                    if (n == 0 && c == 10) return 1;
                    else return n * fact(a,b ,1);
                    a = -16;
                } while (!(c <= 0));
        }"""
        expect = "Error on line 4 col 36: =="
        self.assertTrue(TestParser.test(input, expect, 217))

        input = """demo: function void() {
            if(btl_ppl >= 7) dedung();
            else shout("desaitumlum");
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

        input = """123: function float() {}"""
        expect = "Error on line 1 col 0: 123"
        self.assertTrue(TestParser.test(input, expect, 219))

        input = """experiment: function int() { c = {15_5, 2, 89} <= 1; }"""
        expect = "Error on line 1 col 21: int"
        self.assertTrue(TestParser.test(input, expect, 220))

        input = """main: function auto() { x: void = 57; }"""
        expect = "Error on line 1 col 27: void"
        self.assertTrue(TestParser.test(input, expect, 221))

        input = """nothinghere: array[] of integer;"""
        expect = "Error on line 1 col 19: ]"
        self.assertTrue(TestParser.test(input, expect, 222))

        input = """fact: function void() {
            if(a == 15) else;
            }"""
        expect = "Error on line 2 col 24: else"
        self.assertTrue(TestParser.test(input, expect, 223))

        input = """a: = +2311;"""
        expect = "Error on line 1 col 3: ="
        self.assertTrue(TestParser.test(input, expect, 224))

        input = """fact: function string() {
            if("true") {
                a[1] = a[3] + 2;
                arr[9] = arr[5] + false;
            } else;
        }"""
        expect = "Error on line 5 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 225))

        input = """fact: function integer (n: integer, inherit p: integer){
            a,b,c,d: float;
            do{
                if ((n == 0) && (c + 10)) return 1;
                else return n * fact(a,b ,1);
                a = -16;
            } while (!(c <= 0));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

        input = """gone: function out integer() {}"""
        expect = "Error on line 1 col 15: out"
        self.assertTrue(TestParser.test(input, expect, 227))
        
        input = """main: function void() {
            do goSleeping(),
            while( i + 1 < 2);
            }"""
        expect = "Error on line 2 col 15: goSleeping"
        self.assertTrue(TestParser.test(input, expect, 228))

        input = """eatingPizza(true, false, "hello");"""
        expect = "Error on line 1 col 11: ("
        self.assertTrue(TestParser.test(input, expect, 229))

        input = """fact: function integer (n: integer, inherit p: integer){
                    a,b,c,d: float;
                    do{
                        if (n == 0 && c == 10) return 1;
                        else return n * fact(a,b ,1);
                        a = -16;
                    } while (!(c <= 0));
                }
                main:  function void() {
                    delta: integer = fact();
                }
                X : integer = 65;
            """
        expect = "Error on line 4 col 40: =="
        self.assertTrue(TestParser.test(input, expect, 230))

        input = """fact: function integer (n: integer, inherit p: integer){
                    a,b,c,d: float;
                    do{
                        if (n == 0) return a+b;
                        else return n * fact(a,b ,1);
                        a = -16;
                    } while (!(c <= 0));
                }
                main:  function void() {
                    delta: integer = fact();
                }
                X : integer = 65;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

        input = """fact: function integer() { d[1] = "this is me \\t" + 4; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

        input = """//The thing below is wrong for sure !!
                {x, y, z: integer;}"""
        expect = "Error on line 2 col 16: {"
        self.assertTrue(TestParser.test(input, expect, 233))

        input = """aSmallArray: array[1, 2] of string;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

        input = """fact: function void() {
            if(false)
                7_452 = 8;
            }
        }"""
        expect = "Error on line 3 col 16: 7452"
        self.assertTrue(TestParser.test(input, expect, 235))

        input = """fact: function float() {
            if(true) eat("banana");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

        input = """demo: function auto() {
            i: boolean;
            for(i = i <= a+3 && a == 2, x <= i, x + b) {
            }
        }"""
        expect = "Error on line 3 col 34: =="
        self.assertTrue(TestParser.test(input, expect, 237))

        input = """demo: function auto() {
            i: boolean;
            for(i = 0, x <= i, x + b) {
                if(auto < 3) continuebreak;
            }
        }"""
        expect = "Error on line 4 col 19: auto"
        self.assertTrue(TestParser.test(input, expect, 238))

        input = """act: function void (n: integer){
                    X : integer = 65;
                    while (Iden12 + 1 == 2) 
                    {
                    print("Em khong con yeu Bach Khoa");
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

        input = """fact: function void() {
            if(a) {} else {};
            }"""
        expect = "Error on line 2 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 240))

        input = """fact: function void() {
            if() {} else {};
            }"""
        expect = "Error on line 2 col 15: )"
        self.assertTrue(TestParser.test(input, expect, 241))

        input = """main: function void() { do laugh(); while(true); }"""
        expect = "Error on line 1 col 27: laugh"
        self.assertTrue(TestParser.test(input, expect, 242))

        input = """fact: function void() {
            i: integer;
            for(a = 0 && 75, x + y != 15, i ++) {
                Call("\\b\\r\\n"); //berightnow
                a[4] = 1 && 2;
                break;
            }
        }"""
        expect = "Error on line 3 col 45: +"
        self.assertTrue(TestParser.test(input, expect, 243))

        input = """fact: function void() {
            i: integer;
            for(a = 0.75, x + y != 156, i + 2) {
                Call("\\b\\r\\n"); //a huge comment
                a[4,2] = 1 && 2;
                break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

        input = """main: function void() { fact(integer, "999", "2222"); }"""
        expect = "Error on line 1 col 29: integer"
        self.assertTrue(TestParser.test(input, expect, 245))

        input = """O: float = 5 < 70;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

        input = """float: function boolean(n: integer) {};"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input, expect, 247))

        input = """abc, dvvv, _asdas123: auto = 20, 11, 22;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

        input = """main: function void() { a = a :: 32 < "34" :: "dajjasd"; }"""
        expect = "Error on line 1 col 43: ::"
        self.assertTrue(TestParser.test(input, expect, 249))

        input = """fact: function integer (n: integer){
                a,b,c,d: integer;
                a = -16;
                b = 15 - 4;
                return a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

        input = """fact: function void() { 1[1,1] = "Oanh Tran hehehe \\t"; }"""
        expect = "Error on line 1 col 24: 1"
        self.assertTrue(TestParser.test(input, expect, 251))

        input = """durian: array[1] of boolean() inherit fact {}"""
        expect = "Error on line 1 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 252))

        input = """X_yz, _121, function: floatfloat = 2, false, "true";"""
        expect = "Error on line 1 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 253))

        input = """// A lonely comment :( ;"""
        expect = "Error on line 1 col 24: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 254))

        input = """fact: function integer (n: integer){
                        a,b,c,d: integer;
                        do{
                            a = -16 :: -15;
                        } while (c <= 0);
                        if (n == 0) return 1;
                        else return n * fact(3 + 1);
                    }
                    main:  function void() {
                        delta: integer = fact();
                    }
                    X : integer = 65;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

        input = """tabisnottheculprit: function void() { hellotab = "Tab will kill your app: \\t";//Or sth else will :) }"""
        expect = "Error on line 1 col 101: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 256))

        input = """noParameterAtAll:  function void() {
                    delta: integer = fact();
                    inc();
                    printInteger();
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

        input = """a, b, c: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

        input = """a, b, c: integer || float //Up to you;"""
        expect = "Error on line 1 col 17: ||"
        self.assertTrue(TestParser.test(input, expect, 259))

        input = """function O(){}"""
        expect = "Error on line 1 col 0: function"
        self.assertTrue(TestParser.test(input, expect, 260))

        input = """main: function void() { a = "A string \\t" * 1_021.E+832 && a_12 ! arr[23]; }"""
        expect = "Error on line 1 col 64: !"
        self.assertTrue(TestParser.test(input, expect, 261))

        input = """void lovetheoldone() {  }"""
        expect = "Error on line 1 col 0: void"
        self.assertTrue(TestParser.test(input, expect, 262))

        input = """recursive: function void(recursive();) {
            while(i < 1) increase(i, 1);
            }"""
        expect = "Error on line 1 col 34: ("
        self.assertTrue(TestParser.test(input, expect, 263))

        input = """inheritance: function integer(inherit n: boolean) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

        input = """acorrectfunction: function void() { a = a - 3 + 1 :: 1 + 2 || b % 3e2 / "Siuuuuuuu \\b"; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

        input = """OOP: function integer inherit nothing() {}"""
        expect = "Error on line 1 col 22: inherit"
        self.assertTrue(TestParser.test(input, expect, 266))

        input = """Dio: function theWarudo() { Jotaro(); }"""
        expect = "Error on line 1 col 14: theWarudo"
        self.assertTrue(TestParser.test(input, expect, 267))

        input = """kono: function void(shout("Dio wa")"""
        expect = "Error on line 1 col 25: ("
        self.assertTrue(TestParser.test(input, expect, 268))

        input = """main: function void() { 
        a = arr[23 :: "sleeping \\f" && "beauty" :: 34]; 
        }"""
        expect = "Error on line 2 col 48: ::"
        self.assertTrue(TestParser.test(input, expect, 269))

        input = """parentheseisimportant: function integer (n: integer, inherit p: integer){
                    a,b,c,d: float;
                    do{
                        if ((n == 0) && (c + 10)) return 1;
                        else return n * fact(a,b ,1);
                        a = -16;
                    } while (!(c <= 0));
                }
                main:  function void() {
                    delta: integer = fact();
                }
                X : integer = 65;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

        input = """a: integer = 5 + 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

        input = """b: boolean = 5 && 10;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

        input = """_12abc: function void(123: integer) { a = (a::b)[2]; }"""
        expect = "Error on line 1 col 22: 123"
        self.assertTrue(TestParser.test(input, expect, 273))

        input = """main: function void() { a == -!-foo(01); }"""
        expect = "Error on line 1 col 26: =="
        self.assertTrue(TestParser.test(input, expect, 274))

        input = """demo: function integer(inherit out BK: integer) inherit  21 {}"""
        expect = "Error on line 1 col 57: 21"
        self.assertTrue(TestParser.test(input, expect, 275))

        input = """takoyaki: integer = (-7 + 0) % 91);
            example: function integer(out test: integer) {}"""
        expect = "Error on line 1 col 33: )"
        self.assertTrue(TestParser.test(input, expect, 276))

        input = """a, a_123, if: string = 1 * 2, loveyou(), 1 % 2;"""
        expect = "Error on line 1 col 10: if"
        self.assertTrue(TestParser.test(input, expect, 277))

        input = """main: function void() {
            while(i >= (6+67) ) goout() + goin(2);
            }"""
        expect = "Error on line 2 col 40: +"
        self.assertTrue(TestParser.test(input, expect, 278))

        input = """Another: array[1] of float = "PPL" + "is hard";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

        input = """x, y, z: void;"""
        expect = "Error on line 1 col 9: void"
        self.assertTrue(TestParser.test(input, expect, 280))

        input = """ a,b,c,d: float;
            a,b,c,d: int;"""
        expect = "Error on line 2 col 21: int"
        self.assertTrue(TestParser.test(input, expect, 281))

        input = """fact: function integer (inherit out n: integer, inherit p: integer){
                    a,b,c,d: float;
                    do{
                        if (n + 1 - 2 == 0) return 1;
                        else {return fact(a,b ,1)};
                        a = -16;
                    } while (!(c <= 0 + 8));"""
        expect = "Error on line 5 col 49: }"
        self.assertTrue(TestParser.test(input, expect, 282))

        input = """main: function void() {
            i : integer = 5;
            while(a,b,c == true) a = a + b;
            }"""
        expect = "Error on line 3 col 19: ,"
        self.assertTrue(TestParser.test(input, expect, 283))

        input = """x-ray: boolean = -2 * 1 + 15;
            fact: function integer( test: void) {}"""
        expect = "Error on line 1 col 1: -"
        self.assertTrue(TestParser.test(input, expect, 284))

        input = """function {
            for(i = 1 :: 2, i < 5 + 1, i + 1) {
                continue;
            }
            }"""
        expect = "Error on line 1 col 0: function"
        self.assertTrue(TestParser.test(input, expect, 285))

        input = """main: function void((inherit out bool: boolean)) {}"""
        expect = "Error on line 1 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 286))

        input = """_123, Yasuo, AurelionSol: auto = -5 , 0/21, {"roaming", 1, 7};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

        input = """_123, Yasuo, AurelionSol: auto = -5 , 0/21, main function void(){};"""
        expect = "Error on line 1 col 49: function"
        self.assertTrue(TestParser.test(input, expect, 288))

        input = """fact: float() {}"""
        expect = "Error on line 1 col 11: ("
        self.assertTrue(TestParser.test(input, expect, 289))

        input = """astringarr: array[2,3] boolean;"""
        expect = "Error on line 1 col 23: boolean"
        self.assertTrue(TestParser.test(input, expect, 290))

        input = """_sleepbeast: float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

        input = """main: function void() {
                for(i = -1, i > -10, i - 1) {
                    print(i,)
                }   
            }"""
        expect = "Error on line 3 col 28: )"
        self.assertTrue(TestParser.test(input, expect, 292))

        input = """main: function void() {
            // day la mot cau binh luan chan thanh
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

        input = """main: function void() {
            /* This is a comment line *
        /}"""
        expect = "Error on line 2 col 12: /*"
        self.assertTrue(TestParser.test(input, expect, 294))

        input = """main: function void() {
            "This is a comment line"
        }"""
        expect = "Error on line 2 col 12: This is a comment line"
        self.assertTrue(TestParser.test(input, expect, 295))

        input = """main: function void() {
            {// a = b;}
        }"""
        expect = "Error on line 3 col 9: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 296))

        input = """main: function void() {
            /*
                Begin your code
            */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

        input = """main:  function void() {
                delta: integer = fact();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

        input = """main:  function void() {
                        "c" = "a" :: "b";
                    }"""
        expect = "Error on line 2 col 24: c"
        self.assertTrue(TestParser.test(input, expect, 299))

        input = """main: function void() {
                     c = a + b;// Is this oke?
                     //If not then say it /*wrong*/;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))