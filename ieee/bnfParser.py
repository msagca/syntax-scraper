# Generated from bnfParser.g4 by ANTLR 4.10
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,25,8,0,10,0,12,0,
        28,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,40,8,2,10,2,12,
        2,43,9,2,1,3,1,3,1,4,4,4,48,8,4,11,4,12,4,49,1,5,1,5,1,5,1,5,3,5,
        56,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,10,1,26,0,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,3,3,67,0,26,1,
        0,0,0,2,31,1,0,0,0,4,35,1,0,0,0,6,44,1,0,0,0,8,47,1,0,0,0,10,55,
        1,0,0,0,12,57,1,0,0,0,14,61,1,0,0,0,16,65,1,0,0,0,18,67,1,0,0,0,
        20,69,1,0,0,0,22,25,3,2,1,0,23,25,8,0,0,0,24,22,1,0,0,0,24,23,1,
        0,0,0,25,28,1,0,0,0,26,27,1,0,0,0,26,24,1,0,0,0,27,29,1,0,0,0,28,
        26,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,32,3,16,8,0,32,33,5,3,0,
        0,33,34,3,4,2,0,34,3,1,0,0,0,35,41,3,8,4,0,36,37,3,6,3,0,37,38,3,
        8,4,0,38,40,1,0,0,0,39,36,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,
        42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,45,5,4,0,0,45,7,1,0,0,0,
        46,48,3,10,5,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,
        0,0,0,50,9,1,0,0,0,51,56,3,18,9,0,52,56,3,20,10,0,53,56,3,12,6,0,
        54,56,3,14,7,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,
        0,0,0,56,11,1,0,0,0,57,58,5,5,0,0,58,59,3,4,2,0,59,60,5,6,0,0,60,
        13,1,0,0,0,61,62,5,7,0,0,62,63,3,4,2,0,63,64,5,8,0,0,64,15,1,0,0,
        0,65,66,5,1,0,0,66,17,1,0,0,0,67,68,5,1,0,0,68,19,1,0,0,0,69,70,
        5,11,0,0,70,21,1,0,0,0,5,24,26,41,49,55
    ]

class bnfParser ( Parser ):

    grammarFileName = "bnfParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'::='", "'|'", 
                     "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "CAPITALIZED_WORD", "DOUBLE_COLON_EQUAL", 
                      "VERTICAL_BAR", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
                      "RIGHT_BRACE", "APOSTROPHE", "OTHER", "STRING_TEXT", 
                      "STRING_APOSTROPHE", "STRING_OTHER" ]

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
    CAPITALIZED_WORD=2
    DOUBLE_COLON_EQUAL=3
    VERTICAL_BAR=4
    LEFT_BRACKET=5
    RIGHT_BRACKET=6
    LEFT_BRACE=7
    RIGHT_BRACE=8
    APOSTROPHE=9
    OTHER=10
    STRING_TEXT=11
    STRING_APOSTROPHE=12
    STRING_OTHER=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
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


        def DOUBLE_COLON_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(bnfParser.DOUBLE_COLON_EQUAL)
            else:
                return self.getToken(bnfParser.DOUBLE_COLON_EQUAL, i)

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
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 22
                        self.rule_definition()
                        pass

                    elif la_ == 2:
                        self.state = 23
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==bnfParser.DOUBLE_COLON_EQUAL:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 29
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
            self.state = 31
            self.rule_identifier()
            self.state = 32
            self.match(bnfParser.DOUBLE_COLON_EQUAL)
            self.state = 33
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.alternative()
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self.separator()
                    self.state = 37
                    self.alternative() 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            self.state = 44
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
            self.state = 47 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 46
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bnfParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.rule_reference()
                pass
            elif token in [bnfParser.STRING_TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.keyword_or_punctuation()
                pass
            elif token in [bnfParser.LEFT_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.optional_item()
                pass
            elif token in [bnfParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
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
            self.state = 57
            self.match(bnfParser.LEFT_BRACKET)
            self.state = 58
            self.rule_alternatives()
            self.state = 59
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
            self.state = 61
            self.match(bnfParser.LEFT_BRACE)
            self.state = 62
            self.rule_alternatives()
            self.state = 63
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
            self.state = 65
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
            self.state = 67
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
            self.state = 69
            self.match(bnfParser.STRING_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





