import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_identifier_number(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('_iden_1', "_iden_1,<EOF>", 101))
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('iden', "iden,<EOF>", 102))
    def test_uppercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('IDEN', "IDEN,<EOF>", 103))
    def test_bothuu_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('Iden', "Iden,<EOF>", 104))
    def test_random_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('ThisisareallyrandomIden', "ThisisareallyrandomIden,<EOF>", 105))
    def test_uppercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('IDEN', "IDEN,<EOF>", 106))
    def test_number_simple(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1234', "1234,<EOF>", 107))
    def test_number_underscore_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1_72', "172,<EOF>", 108))
    def test_number_underscore_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1_234_567', "1234567,<EOF>", 109))
    def test_float_simple(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1.234', "1.234,<EOF>", 110))
    def test_float_underscore_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1_7.2', "17.2,<EOF>", 111))
    def test_float_underscore_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1_234_5.67', "12345.67,<EOF>", 112))
    def test_float_exponent_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1.3e10', "1.3e10,<EOF>", 113))
    def test_float_exponent_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('8E-156', "8E-156,<EOF>", 114))
    def test_float_simple_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1_2.234', "12.234,<EOF>", 115))
    def test_float_underscore_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1_7_4_5.2', "1745.2,<EOF>", 116))
    def test_float_underscore_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1111_5.67', "11115.67,<EOF>", 117))
    def test_float_exponent_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1.3e+10', "1.3e+10,<EOF>", 118))
    def test_float_exponent_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('7E+10', "7E+10,<EOF>", 119))
    def test_float_exponent_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('1_5.2E-10', "15.2E-10,<EOF>", 120))
    def test_string_specialcharacter_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Yankee-2017\t"', "Yankee-2017\t,<EOF>", 121))
    def test_string_specialcharacter_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Yankee-2017\n"', "Unclosed String: Yankee-2017", 122))
    def test_string_specialcharacter_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Yankee-2017\t\n"', "Unclosed String: Yankee-2017", 123))
    def test_string_specialcharacter_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Oanh Tran\n"', "Unclosed String: Oanh Tran", 124))
    def test_string_specialcharacter_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"di hoc bai \t\n"', "Unclosed String: di hoc bai ", 125))
    def test_string_specialcharacter_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Yankee-2017-2020\n"', "Unclosed String: Yankee-2017-2020", 126))
    def test_string_specialcharacter_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Tran Ngoc Oanh, dang hoc Bach Khoa"', "Tran Ngoc Oanh, dang hoc Bach Khoa,<EOF>", 127))
    def test_string_specialcharacter_9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Ho va ten: Tran Ngoc Oanh"', "Ho va ten: Tran Ngoc Oanh,<EOF>", 128))
    def test_string_new_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"1 ong sao sang, 2 ong sang sao"', "1 ong sao sang, 2 ong sang sao,<EOF>", 129))
    def test_string_new_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Cung nhau hoc code nao; if else;"', "Cung nhau hoc code nao; if else;,<EOF>", 130))
    def test_identifier_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"daylamotID123"', "daylamotID123,<EOF>", 131))
    def test_identifier_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"_2311_la_sinhnhat_OanhTran"', "_2311_la_sinhnhat_OanhTran,<EOF>", 132))
    def test_identifier_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"DI1NGAYHOC1DANGKHON"', "DI1NGAYHOC1DANGKHON,<EOF>", 133))
    def test_comment_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('//Daylamotbinhluankhongcodaucach', "<EOF>", 134))
    def test_comment_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('//Day la mot binh luan co dau cach', "<EOF>", 135))
    def test_comment_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Daylamotbinhluankhongcodaucach*/', "<EOF>", 136))
    def test_comment_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Day la mot binh luan co dau cach*/', "<EOF>", 137))
    def test_comment_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('//Binh luan co so 1234567', "<EOF>", 138))
    def test_comment_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('//Binh luan co ki tu dac biet 1234567:;;;\'', "<EOF>", 139))
    def test_comment_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Binh luan co so 1234567*/', "<EOF>", 140))
    def test_comment_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Binh luan co ki tu dac biet 13245678;.\'*/', "<EOF>", 141))
    def test_random_wrong_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('Thisis@reallyrandom_bigIden', "Thisis,Error Token @", 142))
    def test_comment_9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Binh luan co so 1234567\nxuong hang thanh cong*/', "<EOF>", 143))
    def test_comment_10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Binh luan co ki tu dac biet 13245678;.\'\nxuong hang thanh cong*/', "<EOF>", 144))
    def test_comment_wrong_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('//Binh luan co so 1___23++++4567', "<EOF>", 145))
    def test_comment_wrong_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('//Binh luan co ki tu dac biet 1234567:;;\'', "<EOF>", 146))
    def test_comment_wrong_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Binh luan co so 1234567\t*/*/', "*/,<EOF>", 147))
    def test_comment_wrong_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*Binh luan co ki tu dac biet 13245678;.\'*/*/', "*/,<EOF>", 148))
    def test_kw_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('void', "void,<EOF>", 149))
    def test_kw_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('auto', "auto,<EOF>", 150))
    def test_kw_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('return', "return,<EOF>", 151))
    def test_kw_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('for', "for,<EOF>", 152))
    def test_kw_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('boolean', "boolean,<EOF>", 153))
    def test_kw_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('boolean', "boolean,<EOF>", 158))
    def test_kw_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('do', "do,<EOF>", 154))
    def test_kw_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('main', "main,<EOF>", 155))    
    def test_kw_9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('if', "if,<EOF>", 156))
    def test_kw_10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('else', "else,<EOF>", 157))
    def test_kw_11(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('array', "array,<EOF>", 159))
    def test_kw_12(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('break', "break,<EOF>", 160))
    def test_kw_13(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('of', "of,<EOF>", 161))    
    def test_kw_14(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('inherit', "inherit,<EOF>", 162))
    def test_kw_15(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('true', "true,<EOF>", 163))
    def test_op_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('+', "+,<EOF>", 164))
    def test_op_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('-', "-,<EOF>", 165))
    def test_op_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('*', "*,<EOF>", 166))
    def test_op_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('==', "==,<EOF>", 167))
    def test_op_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('<=', "<=,<EOF>", 168))
    def test_op_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('>=', ">=,<EOF>", 169))
    def test_op_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/', "/,<EOF>", 170))
    def test_op_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('::', "::,<EOF>", 171))    
    def test_op_9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('||', "||,<EOF>", 172))
    def test_op_10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('&&', "&&,<EOF>", 173))
    def test_op_11(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('%', "%,<EOF>", 174))
    def test_op_12(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('!=', "!=,<EOF>", 175))
    def test_op_13(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('!', "!,<EOF>", 176))    
    def test_op_14(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('>', ">,<EOF>", 177))
    def test_op_15(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('7_xyz', "7,xyz,<EOF>", 178))
    def test_lexer_general(self):
        self.assertTrue(TestLexer.test("aut0;","aut0,;,<EOF>",179))
        self.assertTrue(TestLexer.test("{2.3, 4.2, 105e3}", "{,2.3,,,4.2,,,105e3,},<EOF>", 180))
        self.assertTrue(TestLexer.test("{while (x < 5) x = x + 1;}","{,while,(,x,<,5,),x,=,x,+,1,;,},<EOF>",182))
        self.assertTrue(TestLexer.test("""goo(x - 3; 4.0 / z ");""","goo,(,x,-,3,;,4.0,/,z,Unclosed String: );",183))
        self.assertTrue(TestLexer.test("","<EOF>",184))
        self.assertTrue(TestLexer.test("                     ","<EOF>",185))
        self.assertTrue(TestLexer.test("// love SOS __ILY","<EOF>",186))
        self.assertTrue(TestLexer.test("/* Hello /**/ Tui la mot cuc comment */","Tui,la,mot,cuc,comment,*/,<EOF>",187))
        self.assertTrue(TestLexer.test("// /* I am Oanh Tran OTSC.","<EOF>",188))
        self.assertTrue(TestLexer.test("// /* \n My name is Oanh.   ","My,name,is,Oanh,.,<EOF>",189))
        self.assertTrue(TestLexer.test("// Watch \n // The // movie","<EOF>",190))
        self.assertTrue(TestLexer.test("checkInt: function int (n : integer) {","checkInt,:,function,int,(,n,:,integer,),{,<EOF>",191))
        self.assertTrue(TestLexer.test("if (a == 0 + 1 && b == 2) return;","if,(,a,==,0,+,1,&&,b,==,2,),return,;,<EOF>",192))
        self.assertTrue(TestLexer.test("i : integer;","i,:,integer,;,<EOF>",193))
        self.assertTrue(TestLexer.test("for(i = 2, i * i <= n, i = i + 1)","for,(,i,=,2,,,i,*,i,<=,n,,,i,=,i,+,1,),<EOF>",194))
        self.assertTrue(TestLexer.test("if (n % i == 0) return false;;  ","if,(,n,%,i,==,0,),return,false,;,;,<EOF>",195))
        self.assertTrue(TestLexer.test("true || false;}","true,||,false,;,},<EOF>",196))
        self.assertTrue(TestLexer.test("main: function int() {","main,:,function,int,(,),{,<EOF>",197))
        self.assertTrue(TestLexer.test("n : float = 7.5","n,:,float,=,7.5,<EOF>",198))
        self.assertTrue(TestLexer.test("""n = n + dingu("1.0");   ""","n,=,n,+,dingu,(,1.0,),;,<EOF>",199))
        self.assertTrue(TestLexer.test("hom_nay_lamotngaybuon26/2", "hom_nay_lamotngaybuon26,/,2,<EOF>", 200))