# Generated from bnfParser.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\7\4)\n\4\f\4\16\4,\13\4\3\5\3\5\3\6\6\6\61\n\6\r")
        buf.write("\6\16\6\62\3\7\3\7\3\7\3\7\5\79\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\2\2C\2\33\3\2\2\2\4 \3\2\2\2")
        buf.write("\6$\3\2\2\2\b-\3\2\2\2\n\60\3\2\2\2\f8\3\2\2\2\16:\3\2")
        buf.write("\2\2\20>\3\2\2\2\22B\3\2\2\2\24D\3\2\2\2\26F\3\2\2\2\30")
        buf.write("\32\5\4\3\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\2\2")
        buf.write("\3\37\3\3\2\2\2 !\5\22\n\2!\"\7\4\2\2\"#\5\6\4\2#\5\3")
        buf.write("\2\2\2$*\5\n\6\2%&\5\b\5\2&\'\5\n\6\2\')\3\2\2\2(%\3\2")
        buf.write("\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\7\3\2\2\2,*\3\2\2")
        buf.write("\2-.\7\5\2\2.\t\3\2\2\2/\61\5\f\7\2\60/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\13\3\2\2\2\64")
        buf.write("9\5\24\13\2\659\5\26\f\2\669\5\16\b\2\679\5\20\t\28\64")
        buf.write("\3\2\2\28\65\3\2\2\28\66\3\2\2\28\67\3\2\2\29\r\3\2\2")
        buf.write("\2:;\7\6\2\2;<\5\6\4\2<=\7\7\2\2=\17\3\2\2\2>?\7\b\2\2")
        buf.write("?@\5\6\4\2@A\7\t\2\2A\21\3\2\2\2BC\7\3\2\2C\23\3\2\2\2")
        buf.write("DE\7\3\2\2E\25\3\2\2\2FG\7\f\2\2G\27\3\2\2\2\6\33*\62")
        buf.write("8")
        return buf.getvalue()


class bnfParser ( Parser ):

    grammarFileName = "bnfParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'::='", "'|'", "'['", "']'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "DOUBLE_COLON_EQUAL", "VERTICAL_BAR", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                      "APOSTROPHE", "OTHER", "STRING_TEXT", "STRING_APOSTROPHE", 
                      "STRING_OTHER" ]

    RULE_formal_syntax = 0
    RULE_rule_definition = 1
    RULE_rule_alternatives = 2
    RULE_separator = 3
    RULE_alternative = 4
    RULE_item = 5
    RULE_optional_item = 6
    RULE_repeated_item = 7
    RULE_rule_identifier = 8
    RULE_rule_reference = 9
    RULE_keyword_or_punctuation = 10

    ruleNames =  [ "formal_syntax", "rule_definition", "rule_alternatives", 
                   "separator", "alternative", "item", "optional_item", 
                   "repeated_item", "rule_identifier", "rule_reference", 
                   "keyword_or_punctuation" ]

    EOF = Token.EOF
    IDENTIFIER=1
    DOUBLE_COLON_EQUAL=2
    VERTICAL_BAR=3
    LEFT_BRACKET=4
    RIGHT_BRACKET=5
    LEFT_BRACE=6
    RIGHT_BRACE=7
    APOSTROPHE=8
    OTHER=9
    STRING_TEXT=10
    STRING_APOSTROPHE=11
    STRING_OTHER=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Formal_syntaxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(bnfParser.EOF, 0)

        def rule_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bnfParser.Rule_definitionContext)
            else:
                return self.getTypedRuleContext(bnfParser.Rule_definitionContext,i)


        def getRuleIndex(self):
            return bnfParser.RULE_formal_syntax

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal_syntax" ):
                listener.enterFormal_syntax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal_syntax" ):
                listener.exitFormal_syntax(self)




    def formal_syntax(self):

        localctx = bnfParser.Formal_syntaxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formal_syntax)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==bnfParser.IDENTIFIER:
                self.state = 22
                self.rule_definition()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(bnfParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_identifier(self):
            return self.getTypedRuleContext(bnfParser.Rule_identifierContext,0)


        def DOUBLE_COLON_EQUAL(self):
            return self.getToken(bnfParser.DOUBLE_COLON_EQUAL, 0)

        def rule_alternatives(self):
            return self.getTypedRuleContext(bnfParser.Rule_alternativesContext,0)


        def getRuleIndex(self):
            return bnfParser.RULE_rule_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_definition" ):
                listener.enterRule_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_definition" ):
                listener.exitRule_definition(self)




    def rule_definition(self):

        localctx = bnfParser.Rule_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.rule_identifier()
            self.state = 31
            self.match(bnfParser.DOUBLE_COLON_EQUAL)
            self.state = 32
            self.rule_alternatives()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_alternativesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bnfParser.AlternativeContext)
            else:
                return self.getTypedRuleContext(bnfParser.AlternativeContext,i)


        def separator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bnfParser.SeparatorContext)
            else:
                return self.getTypedRuleContext(bnfParser.SeparatorContext,i)


        def getRuleIndex(self):
            return bnfParser.RULE_rule_alternatives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_alternatives" ):
                listener.enterRule_alternatives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_alternatives" ):
                listener.exitRule_alternatives(self)




    def rule_alternatives(self):

        localctx = bnfParser.Rule_alternativesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rule_alternatives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.alternative()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==bnfParser.VERTICAL_BAR:
                self.state = 35
                self.separator()
                self.state = 36
                self.alternative()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERTICAL_BAR(self):
            return self.getToken(bnfParser.VERTICAL_BAR, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_separator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeparator" ):
                listener.enterSeparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeparator" ):
                listener.exitSeparator(self)




    def separator(self):

        localctx = bnfParser.SeparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_separator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(bnfParser.VERTICAL_BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bnfParser.ItemContext)
            else:
                return self.getTypedRuleContext(bnfParser.ItemContext,i)


        def getRuleIndex(self):
            return bnfParser.RULE_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternative" ):
                listener.enterAlternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternative" ):
                listener.exitAlternative(self)




    def alternative(self):

        localctx = bnfParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alternative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 45
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 48 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_reference(self):
            return self.getTypedRuleContext(bnfParser.Rule_referenceContext,0)


        def keyword_or_punctuation(self):
            return self.getTypedRuleContext(bnfParser.Keyword_or_punctuationContext,0)


        def optional_item(self):
            return self.getTypedRuleContext(bnfParser.Optional_itemContext,0)


        def repeated_item(self):
            return self.getTypedRuleContext(bnfParser.Repeated_itemContext,0)


        def getRuleIndex(self):
            return bnfParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = bnfParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_item)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bnfParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.rule_reference()
                pass
            elif token in [bnfParser.STRING_TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.keyword_or_punctuation()
                pass
            elif token in [bnfParser.LEFT_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.optional_item()
                pass
            elif token in [bnfParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.repeated_item()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(bnfParser.LEFT_BRACKET, 0)

        def rule_alternatives(self):
            return self.getTypedRuleContext(bnfParser.Rule_alternativesContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(bnfParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_optional_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_item" ):
                listener.enterOptional_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_item" ):
                listener.exitOptional_item(self)




    def optional_item(self):

        localctx = bnfParser.Optional_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_optional_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(bnfParser.LEFT_BRACKET)
            self.state = 57
            self.rule_alternatives()
            self.state = 58
            self.match(bnfParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Repeated_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(bnfParser.LEFT_BRACE, 0)

        def rule_alternatives(self):
            return self.getTypedRuleContext(bnfParser.Rule_alternativesContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(bnfParser.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_repeated_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeated_item" ):
                listener.enterRepeated_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeated_item" ):
                listener.exitRepeated_item(self)




    def repeated_item(self):

        localctx = bnfParser.Repeated_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_repeated_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(bnfParser.LEFT_BRACE)
            self.state = 61
            self.rule_alternatives()
            self.state = 62
            self.match(bnfParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(bnfParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_rule_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_identifier" ):
                listener.enterRule_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_identifier" ):
                listener.exitRule_identifier(self)




    def rule_identifier(self):

        localctx = bnfParser.Rule_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rule_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(bnfParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(bnfParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_rule_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_reference" ):
                listener.enterRule_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_reference" ):
                listener.exitRule_reference(self)




    def rule_reference(self):

        localctx = bnfParser.Rule_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_rule_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(bnfParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_or_punctuationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_TEXT(self):
            return self.getToken(bnfParser.STRING_TEXT, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_keyword_or_punctuation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword_or_punctuation" ):
                listener.enterKeyword_or_punctuation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword_or_punctuation" ):
                listener.exitKeyword_or_punctuation(self)




    def keyword_or_punctuation(self):

        localctx = bnfParser.Keyword_or_punctuationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_keyword_or_punctuation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(bnfParser.STRING_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





