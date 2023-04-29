# Generated from c:\Users\admin\MYBK\HK222\Principle of Programming Language_CC04\Ass3\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *;




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01d4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\6")
        buf.write("\2\u0087\n\2\r\2\16\2\u0088\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u009a\n\6\f\6\16")
        buf.write("\6\u009d\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7")
        buf.write("\u00a8\n\7\f\7\16\7\u00ab\13\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\7\67\u0167")
        buf.write("\n\67\f\67\16\67\u016a\13\67\38\38\68\u016e\n8\r8\168")
        buf.write("\u016f\38\78\u0173\n8\f8\168\u0176\138\38\58\u0179\n8")
        buf.write("\39\39\59\u017d\n9\39\39\39\39\59\u0183\n9\59\u0185\n")
        buf.write("9\39\39\3:\3:\7:\u018b\n:\f:\16:\u018e\13:\3;\3;\3;\5")
        buf.write(";\u0193\n;\3;\6;\u0196\n;\r;\16;\u0197\3<\3<\6<\u019c")
        buf.write("\n<\r<\16<\u019d\3<\7<\u01a1\n<\f<\16<\u01a4\13<\5<\u01a6")
        buf.write("\n<\3=\3=\5=\u01aa\n=\3=\3=\3=\3>\3>\6>\u01b1\n>\r>\16")
        buf.write(">\u01b2\3?\3?\3?\3@\3@\3@\7@\u01bb\n@\f@\16@\u01be\13")
        buf.write("@\3@\5@\u01c1\n@\3@\3@\3A\3A\3A\7A\u01c8\nA\fA\16A\u01cb")
        buf.write("\13A\3A\3A\3A\3A\3A\3B\3B\3B\3\u009b\2C\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2w\2y;{\2}\2\177")
        buf.write("<\u0081=\u0083>\3\2\17\5\2\n\f\16\17\"\"\4\2\f\f\16\17")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62\62\3\2\63;\4\2\62;a")
        buf.write("a\3\2\62;\4\2GGgg\5\2\f\f\17\17$$\n\2$$))^^ddhhppttvv")
        buf.write("\3\2$$\7\2\n\f\16\17$$))^^\2\u01e8\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2y\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0086")
        buf.write("\3\2\2\2\5\u008c\3\2\2\2\7\u008f\3\2\2\2\t\u0092\3\2\2")
        buf.write("\2\13\u0095\3\2\2\2\r\u00a3\3\2\2\2\17\u00ae\3\2\2\2\21")
        buf.write("\u00b3\3\2\2\2\23\u00bb\3\2\2\2\25\u00c0\3\2\2\2\27\u00c6")
        buf.write("\3\2\2\2\31\u00cc\3\2\2\2\33\u00d2\3\2\2\2\35\u00d9\3")
        buf.write("\2\2\2\37\u00dd\3\2\2\2!\u00e5\3\2\2\2#\u00e9\3\2\2\2")
        buf.write("%\u00f0\3\2\2\2\'\u00f9\3\2\2\2)\u00fc\3\2\2\2+\u0105")
        buf.write("\3\2\2\2-\u0108\3\2\2\2/\u010d\3\2\2\2\61\u0110\3\2\2")
        buf.write("\2\63\u0116\3\2\2\2\65\u011e\3\2\2\2\67\u0123\3\2\2\2")
        buf.write("9\u0129\3\2\2\2;\u012b\3\2\2\2=\u012d\3\2\2\2?\u0130\3")
        buf.write("\2\2\2A\u0132\3\2\2\2C\u0134\3\2\2\2E\u0137\3\2\2\2G\u0139")
        buf.write("\3\2\2\2I\u013c\3\2\2\2K\u013f\3\2\2\2M\u0141\3\2\2\2")
        buf.write("O\u0144\3\2\2\2Q\u0146\3\2\2\2S\u0148\3\2\2\2U\u014b\3")
        buf.write("\2\2\2W\u014e\3\2\2\2Y\u0150\3\2\2\2[\u0152\3\2\2\2]\u0154")
        buf.write("\3\2\2\2_\u0156\3\2\2\2a\u0158\3\2\2\2c\u015a\3\2\2\2")
        buf.write("e\u015c\3\2\2\2g\u015e\3\2\2\2i\u0160\3\2\2\2k\u0162\3")
        buf.write("\2\2\2m\u0164\3\2\2\2o\u0178\3\2\2\2q\u017c\3\2\2\2s\u0188")
        buf.write("\3\2\2\2u\u018f\3\2\2\2w\u01a5\3\2\2\2y\u01a7\3\2\2\2")
        buf.write("{\u01b0\3\2\2\2}\u01b4\3\2\2\2\177\u01b7\3\2\2\2\u0081")
        buf.write("\u01c4\3\2\2\2\u0083\u01d1\3\2\2\2\u0085\u0087\t\2\2\2")
        buf.write("\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b")
        buf.write("\b\2\2\2\u008b\4\3\2\2\2\u008c\u008d\7\61\2\2\u008d\u008e")
        buf.write("\7,\2\2\u008e\6\3\2\2\2\u008f\u0090\7,\2\2\u0090\u0091")
        buf.write("\7\61\2\2\u0091\b\3\2\2\2\u0092\u0093\7\61\2\2\u0093\u0094")
        buf.write("\7\61\2\2\u0094\n\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097")
        buf.write("\7,\2\2\u0097\u009b\3\2\2\2\u0098\u009a\13\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009e\u009f\7,\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\u00a2\b\6\2\2\u00a2\f\3\2\2\2\u00a3\u00a4")
        buf.write("\7\61\2\2\u00a4\u00a5\7\61\2\2\u00a5\u00a9\3\2\2\2\u00a6")
        buf.write("\u00a8\n\3\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\b\7\2\2\u00ad\16")
        buf.write("\3\2\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7q\2\2\u00b2\20\3\2\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\u00b8\7i\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\22\3\2\2\2\u00bb\u00bc\7x\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7f\2\2\u00bf\24")
        buf.write("\3\2\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7t\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7{\2\2\u00c5\26")
        buf.write("\3\2\2\2\u00c6\u00c7\7d\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7m\2\2\u00cb\30")
        buf.write("\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf")
        buf.write("\7q\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7v\2\2\u00d1\32")
        buf.write("\3\2\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\34\3\2\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7v\2\2\u00dc\36\3\2\2\2\u00dd\u00de")
        buf.write("\7d\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7n\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4 \3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7t\2\2\u00e8\"\3\2\2\2\u00e9\u00ea")
        buf.write("\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7i\2\2\u00ef$\3")
        buf.write("\2\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8\7g\2\2\u00f8&\3")
        buf.write("\2\2\2\u00f9\u00fa\7f\2\2\u00fa\u00fb\7q\2\2\u00fb(\3")
        buf.write("\2\2\2\u00fc\u00fd\7h\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7e\2\2\u0100\u0101\7v\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7q\2\2\u0103\u0104\7p\2\2\u0104*\3")
        buf.write("\2\2\2\u0105\u0106\7q\2\2\u0106\u0107\7h\2\2\u0107,\3")
        buf.write("\2\2\2\u0108\u0109\7g\2\2\u0109\u010a\7n\2\2\u010a\u010b")
        buf.write("\7u\2\2\u010b\u010c\7g\2\2\u010c.\3\2\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7h\2\2\u010f\60\3\2\2\2\u0110\u0111")
        buf.write("\7y\2\2\u0111\u0112\7j\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7n\2\2\u0114\u0115\7g\2\2\u0115\62\3\2\2\2\u0116\u0117")
        buf.write("\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119\7j\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7t\2\2\u011b\u011c\7k\2\2\u011c\u011d")
        buf.write("\7v\2\2\u011d\64\3\2\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120\u0121\7w\2\2\u0121\u0122\7g\2\2\u0122\66")
        buf.write("\3\2\2\2\u0123\u0124\7h\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7n\2\2\u0126\u0127\7u\2\2\u0127\u0128\7g\2\2\u01288\3")
        buf.write("\2\2\2\u0129\u012a\7-\2\2\u012a:\3\2\2\2\u012b\u012c\7")
        buf.write("#\2\2\u012c<\3\2\2\2\u012d\u012e\7#\2\2\u012e\u012f\7")
        buf.write("?\2\2\u012f>\3\2\2\2\u0130\u0131\7/\2\2\u0131@\3\2\2\2")
        buf.write("\u0132\u0133\7,\2\2\u0133B\3\2\2\2\u0134\u0135\7(\2\2")
        buf.write("\u0135\u0136\7(\2\2\u0136D\3\2\2\2\u0137\u0138\7>\2\2")
        buf.write("\u0138F\3\2\2\2\u0139\u013a\7~\2\2\u013a\u013b\7~\2\2")
        buf.write("\u013bH\3\2\2\2\u013c\u013d\7>\2\2\u013d\u013e\7?\2\2")
        buf.write("\u013eJ\3\2\2\2\u013f\u0140\7\61\2\2\u0140L\3\2\2\2\u0141")
        buf.write("\u0142\7?\2\2\u0142\u0143\7?\2\2\u0143N\3\2\2\2\u0144")
        buf.write("\u0145\7@\2\2\u0145P\3\2\2\2\u0146\u0147\7\'\2\2\u0147")
        buf.write("R\3\2\2\2\u0148\u0149\7@\2\2\u0149\u014a\7?\2\2\u014a")
        buf.write("T\3\2\2\2\u014b\u014c\7<\2\2\u014c\u014d\7<\2\2\u014d")
        buf.write("V\3\2\2\2\u014e\u014f\7\60\2\2\u014fX\3\2\2\2\u0150\u0151")
        buf.write("\7<\2\2\u0151Z\3\2\2\2\u0152\u0153\7.\2\2\u0153\\\3\2")
        buf.write("\2\2\u0154\u0155\7=\2\2\u0155^\3\2\2\2\u0156\u0157\7*")
        buf.write("\2\2\u0157`\3\2\2\2\u0158\u0159\7+\2\2\u0159b\3\2\2\2")
        buf.write("\u015a\u015b\7}\2\2\u015bd\3\2\2\2\u015c\u015d\7\177\2")
        buf.write("\2\u015df\3\2\2\2\u015e\u015f\7?\2\2\u015fh\3\2\2\2\u0160")
        buf.write("\u0161\7]\2\2\u0161j\3\2\2\2\u0162\u0163\7_\2\2\u0163")
        buf.write("l\3\2\2\2\u0164\u0168\t\4\2\2\u0165\u0167\t\5\2\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169n\3\2\2\2\u016a\u0168\3\2\2")
        buf.write("\2\u016b\u0179\t\6\2\2\u016c\u016e\t\7\2\2\u016d\u016c")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0174\3\2\2\2\u0171\u0173\t\b\2\2")
        buf.write("\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0177\u0179\b8\3\2\u0178\u016b\3\2\2\2\u0178")
        buf.write("\u016d\3\2\2\2\u0179p\3\2\2\2\u017a\u017d\5w<\2\u017b")
        buf.write("\u017d\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2")
        buf.write("\u017d\u0184\3\2\2\2\u017e\u0185\5s:\2\u017f\u0185\5u")
        buf.write(";\2\u0180\u0182\5s:\2\u0181\u0183\5u;\2\u0182\u0181\3")
        buf.write("\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u017e")
        buf.write("\3\2\2\2\u0184\u017f\3\2\2\2\u0184\u0180\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0187\b9\4\2\u0187r\3\2\2\2\u0188")
        buf.write("\u018c\7\60\2\2\u0189\u018b\t\t\2\2\u018a\u0189\3\2\2")
        buf.write("\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018dt\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0192")
        buf.write("\t\n\2\2\u0190\u0193\5? \2\u0191\u0193\59\35\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0195\3\2\2\2\u0194\u0196\t\t\2\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3")
        buf.write("\2\2\2\u0198v\3\2\2\2\u0199\u01a6\t\6\2\2\u019a\u019c")
        buf.write("\t\7\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a2\3\2\2\2")
        buf.write("\u019f\u01a1\t\b\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a4\3")
        buf.write("\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a6")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u0199\3\2\2\2\u01a5")
        buf.write("\u019b\3\2\2\2\u01a6x\3\2\2\2\u01a7\u01a9\7$\2\2\u01a8")
        buf.write("\u01aa\5{>\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ac\7$\2\2\u01ac\u01ad\b=\5\2\u01ad")
        buf.write("z\3\2\2\2\u01ae\u01b1\n\13\2\2\u01af\u01b1\5}?\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3|\3\2\2")
        buf.write("\2\u01b4\u01b5\7^\2\2\u01b5\u01b6\t\f\2\2\u01b6~\3\2\2")
        buf.write("\2\u01b7\u01bc\t\r\2\2\u01b8\u01bb\n\16\2\2\u01b9\u01bb")
        buf.write("\5}?\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01be")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c1\7\2\2\3")
        buf.write("\u01c0\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3")
        buf.write("\2\2\2\u01c2\u01c3\b@\6\2\u01c3\u0080\3\2\2\2\u01c4\u01c9")
        buf.write("\t\r\2\2\u01c5\u01c8\n\16\2\2\u01c6\u01c8\5}?\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3")
        buf.write("\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\7^\2\2\u01cd\u01ce")
        buf.write("\n\f\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\bA\7\2\u01d0")
        buf.write("\u0082\3\2\2\2\u01d1\u01d2\13\2\2\2\u01d2\u01d3\bB\b\2")
        buf.write("\u01d3\u0084\3\2\2\2\33\2\u0088\u009b\u00a9\u0168\u016f")
        buf.write("\u0174\u0178\u017c\u0182\u0184\u018c\u0192\u0197\u019d")
        buf.write("\u01a2\u01a5\u01a9\u01b0\u01b2\u01ba\u01bc\u01c0\u01c7")
        buf.write("\u01c9\t\b\2\2\38\2\39\3\3=\4\3@\5\3A\6\3B\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    LCOMMENTC = 2
    RCOMMENTC = 3
    COMMENTCPPSYM = 4
    COMMENTC = 5
    COMMENTCPP = 6
    AUTO = 7
    INTEGER = 8
    VOID = 9
    ARRAY = 10
    BREAK = 11
    FLOAT = 12
    RETURN = 13
    OUT = 14
    BOOLEAN = 15
    FOR = 16
    STRING = 17
    CONTINUE = 18
    DO = 19
    FUNCTION = 20
    OF = 21
    ELSE = 22
    IF = 23
    WHILE = 24
    INHERIT = 25
    TRUE = 26
    FALSE = 27
    PLUS = 28
    NOT = 29
    NOTEQ = 30
    MINUS = 31
    MUL = 32
    AND = 33
    SMALLER = 34
    OR = 35
    SMALLEREQ = 36
    DIVIDE = 37
    EQ = 38
    GREATER = 39
    MODULO = 40
    GREATEREQ = 41
    STRCONCAT = 42
    DOT = 43
    COLON = 44
    COMMA = 45
    SEMI = 46
    LPAREN = 47
    RPAREN = 48
    LCURLY = 49
    RCURLY = 50
    ASSIGN = 51
    LSQBRACKET = 52
    RSQBRRACKET = 53
    ID = 54
    INTLIT = 55
    FLOATLIT = 56
    STRLIT = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'/*'", "'*/'", "'//'", "'auto'", "'integer'", "'void'", "'array'", 
            "'break'", "'float'", "'return'", "'out'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'function'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'true'", "'false'", "'+'", 
            "'!'", "'!='", "'-'", "'*'", "'&&'", "'<'", "'||'", "'<='", 
            "'/'", "'=='", "'>'", "'%'", "'>='", "'::'", "'.'", "':'", "','", 
            "';'", "'('", "')'", "'{'", "'}'", "'='", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "LCOMMENTC", "RCOMMENTC", "COMMENTCPPSYM", "COMMENTC", 
            "COMMENTCPP", "AUTO", "INTEGER", "VOID", "ARRAY", "BREAK", "FLOAT", 
            "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
            "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", "TRUE", 
            "FALSE", "PLUS", "NOT", "NOTEQ", "MINUS", "MUL", "AND", "SMALLER", 
            "OR", "SMALLEREQ", "DIVIDE", "EQ", "GREATER", "MODULO", "GREATEREQ", 
            "STRCONCAT", "DOT", "COLON", "COMMA", "SEMI", "LPAREN", "RPAREN", 
            "LCURLY", "RCURLY", "ASSIGN", "LSQBRACKET", "RSQBRRACKET", "ID", 
            "INTLIT", "FLOATLIT", "STRLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "WS", "LCOMMENTC", "RCOMMENTC", "COMMENTCPPSYM", "COMMENTC", 
                  "COMMENTCPP", "AUTO", "INTEGER", "VOID", "ARRAY", "BREAK", 
                  "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
                  "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", 
                  "INHERIT", "TRUE", "FALSE", "PLUS", "NOT", "NOTEQ", "MINUS", 
                  "MUL", "AND", "SMALLER", "OR", "SMALLEREQ", "DIVIDE", 
                  "EQ", "GREATER", "MODULO", "GREATEREQ", "STRCONCAT", "DOT", 
                  "COLON", "COMMA", "SEMI", "LPAREN", "RPAREN", "LCURLY", 
                  "RCURLY", "ASSIGN", "LSQBRACKET", "RSQBRRACKET", "ID", 
                  "INTLIT", "FLOATLIT", "DECIMAL", "EXP", "INTPART", "STRLIT", 
                  "StrChar", "EscSe", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.INTLIT_action 
            actions[55] = self.FLOATLIT_action 
            actions[59] = self.STRLIT_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                y = str(self.text)
                raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise ErrorToken(self.text)

     


