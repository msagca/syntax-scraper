# Generated from bnfLexer.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("O\b\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\6\13>\n\13\r\13\16\13")
        buf.write("?\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\2\2\17\4\3\6\4\b\5\n\6\f\7\16\b\20\t\22\n\24")
        buf.write("\13\26\f\30\2\32\r\34\16\4\2\3\5\4\2C\\c|\6\2\62;C\\a")
        buf.write("ac|\4\2))^^\2O\2\4\3\2\2\2\2\6\3\2\2\2\2\b\3\2\2\2\2\n")
        buf.write("\3\2\2\2\2\f\3\2\2\2\2\16\3\2\2\2\2\20\3\2\2\2\2\22\3")
        buf.write("\2\2\2\2\24\3\2\2\2\3\26\3\2\2\2\3\30\3\2\2\2\3\32\3\2")
        buf.write("\2\2\3\34\3\2\2\2\4\36\3\2\2\2\6%\3\2\2\2\b)\3\2\2\2\n")
        buf.write("+\3\2\2\2\f-\3\2\2\2\16/\3\2\2\2\20\61\3\2\2\2\22\63\3")
        buf.write("\2\2\2\248\3\2\2\2\26=\3\2\2\2\30A\3\2\2\2\32F\3\2\2\2")
        buf.write("\34K\3\2\2\2\36\"\t\2\2\2\37!\t\3\2\2 \37\3\2\2\2!$\3")
        buf.write("\2\2\2\" \3\2\2\2\"#\3\2\2\2#\5\3\2\2\2$\"\3\2\2\2%&\7")
        buf.write("<\2\2&\'\7<\2\2\'(\7?\2\2(\7\3\2\2\2)*\7~\2\2*\t\3\2\2")
        buf.write("\2+,\7]\2\2,\13\3\2\2\2-.\7_\2\2.\r\3\2\2\2/\60\7}\2\2")
        buf.write("\60\17\3\2\2\2\61\62\7\177\2\2\62\21\3\2\2\2\63\64\7)")
        buf.write("\2\2\64\65\3\2\2\2\65\66\b\t\2\2\66\67\b\t\3\2\67\23\3")
        buf.write("\2\2\289\13\2\2\29:\3\2\2\2:;\b\n\4\2;\25\3\2\2\2<>\n")
        buf.write("\4\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\27\3\2")
        buf.write("\2\2AB\7^\2\2BC\t\4\2\2CD\3\2\2\2DE\b\f\5\2E\31\3\2\2")
        buf.write("\2FG\7)\2\2GH\3\2\2\2HI\b\r\2\2IJ\b\r\6\2J\33\3\2\2\2")
        buf.write("KL\13\2\2\2LM\3\2\2\2MN\b\16\4\2N\35\3\2\2\2\6\2\3\"?")
        buf.write("\7\2\3\2\4\3\2\b\2\2\t\f\2\4\2\2")
        return buf.getvalue()


class bnfLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING_MODE = 1

    IDENTIFIER = 1
    DOUBLE_COLON_EQUAL = 2
    VERTICAL_BAR = 3
    LEFT_BRACKET = 4
    RIGHT_BRACKET = 5
    LEFT_BRACE = 6
    RIGHT_BRACE = 7
    APOSTROPHE = 8
    OTHER = 9
    STRING_TEXT = 10
    STRING_APOSTROPHE = 11
    STRING_OTHER = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "STRING_MODE" ]

    literalNames = [ "<INVALID>",
            "'::='", "'|'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "DOUBLE_COLON_EQUAL", "VERTICAL_BAR", "LEFT_BRACKET", 
            "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "APOSTROPHE", 
            "OTHER", "STRING_TEXT", "STRING_APOSTROPHE", "STRING_OTHER" ]

    ruleNames = [ "IDENTIFIER", "DOUBLE_COLON_EQUAL", "VERTICAL_BAR", "LEFT_BRACKET", 
                  "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "APOSTROPHE", 
                  "OTHER", "STRING_TEXT", "STRING_ESCAPE", "STRING_APOSTROPHE", 
                  "STRING_OTHER" ]

    grammarFileName = "bnfLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


