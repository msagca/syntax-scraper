# -*- coding: utf-8 -*-

import re
from antlr4 import *
if __name__ is not None and "." in __name__:
	from .bnfParser import bnfParser
	from .bnfParserVisitor import bnfParserVisitor
else:
	from bnfParser import bnfParser
	from bnfParserVisitor import bnfParserVisitor

class Scraper(bnfParserVisitor):

	def __init__(self):
		super().__init__()
		self.hier_level = 0

	def visit(self, tree):
		return tree.accept(self)

	def visitChildren(self, node):
		text = ''
		n = node.getChildCount()
		for i in range(n):
			if i > 0:
				text += ' '
			c = node.getChild(i)
			result = c.accept(self)
			if result == None:
				return "'Failed to parse!'"
			text += result
		return text

	def visitTerminal(self, node):
		return node.getText()

	def visitFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
		text = ''
		for rule in ctx.rule_definition():
			text += '\n' + self.visit(rule)
		return text

	def visitRule_definition(self, ctx:bnfParser.Rule_definitionContext):
		return self.visit(ctx.rule_identifier()) + '\n\t: ' + self.visit(ctx.rule_alternatives()) + '\n\t;'

	def visitRule_alternatives(self, ctx:bnfParser.Rule_alternativesContext):
		if self.hier_level == 0:
			text = ''
			for i, alt in enumerate(ctx.alternative()):
				if i > 0:
					text += '\n\t| '
				text += self.visit(alt)
			return text
		else:
			return self.visitChildren(ctx)

	def visitAlternative(self, ctx:bnfParser.AlternativeContext):
		return self.visitChildren(ctx)

	def visitItem(self, ctx:bnfParser.ItemContext):
		return self.visitChildren(ctx)

	def visitOptional_item(self, ctx:bnfParser.Optional_itemContext):
		self.hier_level += 1
		text = self.visit(ctx.rule_alternatives())
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			text = '( ' + text + ' )'
		text += '?'
		self.hier_level -= 1
		return text

	def visitRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
		self.hier_level += 1
		text = self.visit(ctx.rule_alternatives())
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			text = '( ' + text + ' )'
		text += '*'
		self.hier_level -= 1
		return text

	def visitRule_identifier(self, ctx:bnfParser.Rule_identifierContext):
		return self.visitChildren(ctx)

	def visitRule_reference(self, ctx:bnfParser.Rule_referenceContext):
		return self.visitChildren(ctx)

	def visitKeyword_or_punctuation(self, ctx:bnfParser.Keyword_or_punctuationContext):
		return '\'' + self.visitChildren(ctx) + '\''
