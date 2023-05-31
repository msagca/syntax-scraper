# Generated from bnfParser.g4 by ANTLR 4.13.0
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
        4,1,14,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,1,
        3,4,3,43,8,3,11,3,12,3,44,1,4,1,4,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,24,0,10,0,2,4,
        6,8,10,12,14,16,18,0,1,1,0,4,4,63,0,24,1,0,0,0,2,29,1,0,0,0,4,33,
        1,0,0,0,6,42,1,0,0,0,8,50,1,0,0,0,10,52,1,0,0,0,12,56,1,0,0,0,14,
        60,1,0,0,0,16,62,1,0,0,0,18,64,1,0,0,0,20,23,3,2,1,0,21,23,8,0,0,
        0,22,20,1,0,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,25,1,0,0,0,24,22,
        1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,
        30,3,14,7,0,30,31,5,4,0,0,31,32,3,4,2,0,32,3,1,0,0,0,33,38,3,6,3,
        0,34,35,5,5,0,0,35,37,3,6,3,0,36,34,1,0,0,0,37,40,1,0,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,43,3,8,4,0,42,
        41,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,7,1,0,0,
        0,46,51,3,16,8,0,47,51,3,18,9,0,48,51,3,10,5,0,49,51,3,12,6,0,50,
        46,1,0,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,9,1,0,0,
        0,52,53,5,6,0,0,53,54,3,4,2,0,54,55,5,7,0,0,55,11,1,0,0,0,56,57,
        5,8,0,0,57,58,3,4,2,0,58,59,5,9,0,0,59,13,1,0,0,0,60,61,5,1,0,0,
        61,15,1,0,0,0,62,63,5,1,0,0,63,17,1,0,0,0,64,65,5,12,0,0,65,19,1,
        0,0,0,5,22,24,38,44,50
    ]

class bnfParser ( Parser ):

    grammarFileName = "bnfParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'::='", "'|'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "CAPITALIZED_WORD", "SECTION_REFERENCE", 
                      "DOUBLE_COLON_EQUAL", "VERTICAL_BAR", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "APOSTROPHE", 
                      "OTHER", "STRING_TEXT", "STRING_APOSTROPHE", "STRING_OTHER" ]

    RULE_formal_syntax = 0
    RULE_rule_definition = 1
    RULE_rule_alternatives = 2
    RULE_alternative = 3
    RULE_item = 4
    RULE_optional_item = 5
    RULE_repeated_item = 6
    RULE_rule_identifier = 7
    RULE_rule_reference = 8
    RULE_keyword_or_punctuation = 9

    ruleNames =  [ "formal_syntax", "rule_definition", "rule_alternatives", 
                   "alternative", "item", "optional_item", "repeated_item", 
                   "rule_identifier", "rule_reference", "keyword_or_punctuation" ]

    EOF = Token.EOF
    IDENTIFIER=1
    CAPITALIZED_WORD=2
    SECTION_REFERENCE=3
    DOUBLE_COLON_EQUAL=4
    VERTICAL_BAR=5
    LEFT_BRACKET=6
    RIGHT_BRACKET=7
    LEFT_BRACE=8
    RIGHT_BRACE=9
    APOSTROPHE=10
    OTHER=11
    STRING_TEXT=12
    STRING_APOSTROPHE=13
    STRING_OTHER=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_syntax" ):
                return visitor.visitFormal_syntax(self)
            else:
                return visitor.visitChildren(self)




    def formal_syntax(self):

        localctx = bnfParser.Formal_syntaxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formal_syntax)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 20
                        self.rule_definition()
                        pass

                    elif la_ == 2:
                        self.state = 21
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==4:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 27
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_definition" ):
                return visitor.visitRule_definition(self)
            else:
                return visitor.visitChildren(self)




    def rule_definition(self):

        localctx = bnfParser.Rule_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.rule_identifier()
            self.state = 30
            self.match(bnfParser.DOUBLE_COLON_EQUAL)
            self.state = 31
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


        def VERTICAL_BAR(self, i:int=None):
            if i is None:
                return self.getTokens(bnfParser.VERTICAL_BAR)
            else:
                return self.getToken(bnfParser.VERTICAL_BAR, i)

        def getRuleIndex(self):
            return bnfParser.RULE_rule_alternatives

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_alternatives" ):
                return visitor.visitRule_alternatives(self)
            else:
                return visitor.visitChildren(self)




    def rule_alternatives(self):

        localctx = bnfParser.Rule_alternativesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rule_alternatives)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.alternative()
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.match(bnfParser.VERTICAL_BAR)
                    self.state = 35
                    self.alternative() 
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternative" ):
                return visitor.visitAlternative(self)
            else:
                return visitor.visitChildren(self)




    def alternative(self):

        localctx = bnfParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_alternative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 41
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 44 
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = bnfParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.rule_reference()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.keyword_or_punctuation()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.optional_item()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_item" ):
                return visitor.visitOptional_item(self)
            else:
                return visitor.visitChildren(self)




    def optional_item(self):

        localctx = bnfParser.Optional_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_optional_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(bnfParser.LEFT_BRACKET)
            self.state = 53
            self.rule_alternatives()
            self.state = 54
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeated_item" ):
                return visitor.visitRepeated_item(self)
            else:
                return visitor.visitChildren(self)




    def repeated_item(self):

        localctx = bnfParser.Repeated_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_repeated_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(bnfParser.LEFT_BRACE)
            self.state = 57
            self.rule_alternatives()
            self.state = 58
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_identifier" ):
                return visitor.visitRule_identifier(self)
            else:
                return visitor.visitChildren(self)




    def rule_identifier(self):

        localctx = bnfParser.Rule_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rule_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_reference" ):
                return visitor.visitRule_reference(self)
            else:
                return visitor.visitChildren(self)




    def rule_reference(self):

        localctx = bnfParser.Rule_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rule_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_or_punctuation" ):
                return visitor.visitKeyword_or_punctuation(self)
            else:
                return visitor.visitChildren(self)




    def keyword_or_punctuation(self):

        localctx = bnfParser.Keyword_or_punctuationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_keyword_or_punctuation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(bnfParser.STRING_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





