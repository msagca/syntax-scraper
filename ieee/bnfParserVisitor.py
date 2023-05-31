# Generated from bnfParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .bnfParser import bnfParser
else:
    from bnfParser import bnfParser

# This class defines a complete generic visitor for a parse tree produced by bnfParser.

class bnfParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by bnfParser#formal_syntax.
    def visitFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#rule_definition.
    def visitRule_definition(self, ctx:bnfParser.Rule_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#rule_alternatives.
    def visitRule_alternatives(self, ctx:bnfParser.Rule_alternativesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#alternative.
    def visitAlternative(self, ctx:bnfParser.AlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#item.
    def visitItem(self, ctx:bnfParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#optional_item.
    def visitOptional_item(self, ctx:bnfParser.Optional_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#repeated_item.
    def visitRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#rule_identifier.
    def visitRule_identifier(self, ctx:bnfParser.Rule_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#rule_reference.
    def visitRule_reference(self, ctx:bnfParser.Rule_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bnfParser#keyword_or_punctuation.
    def visitKeyword_or_punctuation(self, ctx:bnfParser.Keyword_or_punctuationContext):
        return self.visitChildren(ctx)



del bnfParser