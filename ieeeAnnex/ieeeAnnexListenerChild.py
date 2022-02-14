# -*- coding: utf-8 -*-

from antlr4 import *
if __name__ is not None and "." in __name__:
	from .ieeeAnnexParser import ieeeAnnexParser
	from .ieeeAnnexListener import ieeeAnnexListener
else:
	from ieeeAnnexParser import ieeeAnnexParser
	from ieeeAnnexListener import ieeeAnnexListener

class ieeeAnnexListenerChild(ieeeAnnexListener):

	def __init__(self, name:str):
		super().__init__()
		self.name = name
		self.rule_tokens = []
		self.alt_stack = []
		self.grammar_definition = ''

	def enterFormal_syntax(self, ctx:ieeeAnnexParser.Formal_syntaxContext):
		self.grammar_definition += f'grammar {self.name};\n'

	def exitRule_definition(self, ctx:ieeeAnnexParser.Rule_definitionContext):
		rule_name = ctx.rule_identifier().getText()
		rule_alts = ''
		num_tokens = len(self.rule_tokens)
		for tt in self.rule_tokens:
			rule_alts += tt
		self.grammar_definition += f'\n{rule_name}\n\t:{rule_alts}\n\t;\n'
		self.rule_tokens = []

	def exitSeparator(self, ctx:ieeeAnnexParser.SeparatorContext):
		if not self.alt_stack:
			self.rule_tokens.append('\n\t')
		else:
			self.rule_tokens.append(' ')
		self.rule_tokens.append('|')

	def enterOptional_item(self, ctx:ieeeAnnexParser.Optional_itemContext):
		self.alt_stack.append('[')
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' (')

	def exitOptional_item(self, ctx:ieeeAnnexParser.Optional_itemContext):
		self.alt_stack.pop()
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' )')
		self.rule_tokens.append('?')

	def enterRepeated_item(self, ctx:ieeeAnnexParser.Repeated_itemContext):
		self.alt_stack.append('{')
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' (')

	def exitRepeated_item(self, ctx:ieeeAnnexParser.Repeated_itemContext):
		self.alt_stack.pop()
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' )')
		self.rule_tokens.append('*')

	def enterRule_reference(self, ctx:ieeeAnnexParser.Rule_referenceContext):
		self.rule_tokens.append(' ' + ctx.getText())

	def enterKeyword_or_punctuation(self, ctx:ieeeAnnexParser.Keyword_or_punctuationContext):
		self.rule_tokens.append(' ' + ctx.getText())
