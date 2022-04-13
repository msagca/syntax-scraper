# Generated from bnfParser.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .bnfParser import bnfParser
else:
    from bnfParser import bnfParser

# This class defines a complete listener for a parse tree produced by bnfParser.
class bnfParserListener(ParseTreeListener):

    # Enter a parse tree produced by bnfParser#formal_syntax.
    def enterFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
        pass

    # Exit a parse tree produced by bnfParser#formal_syntax.
    def exitFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
        pass


    # Enter a parse tree produced by bnfParser#rule_definition.
    def enterRule_definition(self, ctx:bnfParser.Rule_definitionContext):
        pass

    # Exit a parse tree produced by bnfParser#rule_definition.
    def exitRule_definition(self, ctx:bnfParser.Rule_definitionContext):
        pass


    # Enter a parse tree produced by bnfParser#rule_alternatives.
    def enterRule_alternatives(self, ctx:bnfParser.Rule_alternativesContext):
        pass

    # Exit a parse tree produced by bnfParser#rule_alternatives.
    def exitRule_alternatives(self, ctx:bnfParser.Rule_alternativesContext):
        pass


    # Enter a parse tree produced by bnfParser#separator.
    def enterSeparator(self, ctx:bnfParser.SeparatorContext):
        pass

    # Exit a parse tree produced by bnfParser#separator.
    def exitSeparator(self, ctx:bnfParser.SeparatorContext):
        pass


    # Enter a parse tree produced by bnfParser#alternative.
    def enterAlternative(self, ctx:bnfParser.AlternativeContext):
        pass

    # Exit a parse tree produced by bnfParser#alternative.
    def exitAlternative(self, ctx:bnfParser.AlternativeContext):
        pass


    # Enter a parse tree produced by bnfParser#item.
    def enterItem(self, ctx:bnfParser.ItemContext):
        pass

    # Exit a parse tree produced by bnfParser#item.
    def exitItem(self, ctx:bnfParser.ItemContext):
        pass


    # Enter a parse tree produced by bnfParser#optional_item.
    def enterOptional_item(self, ctx:bnfParser.Optional_itemContext):
        pass

    # Exit a parse tree produced by bnfParser#optional_item.
    def exitOptional_item(self, ctx:bnfParser.Optional_itemContext):
        pass


    # Enter a parse tree produced by bnfParser#repeated_item.
    def enterRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
        pass

    # Exit a parse tree produced by bnfParser#repeated_item.
    def exitRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
        pass


    # Enter a parse tree produced by bnfParser#rule_identifier.
    def enterRule_identifier(self, ctx:bnfParser.Rule_identifierContext):
        pass

    # Exit a parse tree produced by bnfParser#rule_identifier.
    def exitRule_identifier(self, ctx:bnfParser.Rule_identifierContext):
        pass


    # Enter a parse tree produced by bnfParser#rule_reference.
    def enterRule_reference(self, ctx:bnfParser.Rule_referenceContext):
        pass

    # Exit a parse tree produced by bnfParser#rule_reference.
    def exitRule_reference(self, ctx:bnfParser.Rule_referenceContext):
        pass


    # Enter a parse tree produced by bnfParser#keyword_or_punctuation.
    def enterKeyword_or_punctuation(self, ctx:bnfParser.Keyword_or_punctuationContext):
        pass

    # Exit a parse tree produced by bnfParser#keyword_or_punctuation.
    def exitKeyword_or_punctuation(self, ctx:bnfParser.Keyword_or_punctuationContext):
        pass



del bnfParser