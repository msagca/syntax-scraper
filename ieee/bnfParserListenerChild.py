# -*- coding: utf-8 -*-

from antlr4 import *
if __name__ is not None and "." in __name__:
	from .bnfParser import bnfParser
	from .bnfParserListener import bnfParserListener
else:
	from bnfParser import bnfParser
	from bnfParserListener import bnfParserListener

class bnfParserListenerChild(bnfParserListener):

	def __init__(self, grammar_name:str):
		super().__init__()
		self.grammar_name = grammar_name
		self.grammar_text = ''
		self.grammar_rules = {}
		self.rule_tokens = []
		self.alt_stack = []

	def enterFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
		self.grammar_text += f'grammar {self.grammar_name};\n'

	def exitFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
		for rule in self.grammar_rules:
			self.grammar_text += f'\n{rule}\n\t:'
			for token in self.grammar_rules[rule]:
				self.grammar_text += token
			self.grammar_text += '\n\t;\n'

	def exitRule_definition(self, ctx:bnfParser.Rule_definitionContext):
		self.grammar_rules[ctx.rule_identifier().getText()] = self.rule_tokens.copy()
		self.rule_tokens = []

	def exitSeparator(self, ctx:bnfParser.SeparatorContext):
		if not self.alt_stack:
			self.rule_tokens.extend(['\n', '\t'])
		else:
			self.rule_tokens.append(' ')
		self.rule_tokens.append('|')

	def enterOptional_item(self, ctx:bnfParser.Optional_itemContext):
		self.alt_stack.append('[')
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.extend([' ', '('])

	def exitOptional_item(self, ctx:bnfParser.Optional_itemContext):
		self.alt_stack.pop()
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.extend([' ', ')'])
		self.rule_tokens.append('?')

	def enterRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
		self.alt_stack.append('{')
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.extend([' ', '('])

	def exitRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
		self.alt_stack.pop()
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.extend([' ', ')'])
		self.rule_tokens.append('*')

	def enterRule_reference(self, ctx:bnfParser.Rule_referenceContext):
		self.rule_tokens.extend([' ', ctx.getText()])

	def enterKeyword_or_punctuation(self, ctx:bnfParser.Keyword_or_punctuationContext):
		self.rule_tokens.extend([' ', '\'', ctx.getText(), '\''])
