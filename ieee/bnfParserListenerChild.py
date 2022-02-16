# -*- coding: utf-8 -*-

from antlr4 import *
import random
if __name__ is not None and "." in __name__:
	from .bnfParser import bnfParser
	from .bnfParserListener import bnfParserListener
else:
	from bnfParser import bnfParser
	from bnfParserListener import bnfParserListener

class bnfParserListenerChild(bnfParserListener):

	def __init__(self, grammar_name:str, grammar_type:str):
		super().__init__()
		self.grammar_name = grammar_name
		self.grammar_type = grammar_type
		self.rule_tokens = []
		self.alt_stack = []
		self.parser_rules = {}
		self.lexer_tokens = set()
		self.parser_grammar = ''
		self.lexer_grammar = ''
		self.symbols = {'0':'ZERO', '1':'ONE', '2':'TWO', '3':'THREE', '4':'FOUR', '5':'FIVE', '6':'SIX', '7':'SEVEN', '8':'EIGHT', '9':'NINE', '!':'EM', '"':'DQ', '#':'HA', '$':'DL', '%':'MO', '&':'AM', '\'':'AP', '(':'LP', ')':'RP', '*':'AS', '+':'PL', ',':'CO', '-':'MI', '.':'DT', '/':'SL', ':':'CL', ';':'SC', '<':'LT', '=':'EQ', '>':'GT', '?':'QM', '@':'AT', '[':'LB', '\\':'BS', ']':'RB', '^':'CA', '_':'UN', '`':'GA', '{':'LC', '|':'VL', '}':'RC', '~':'TI'}

	def enterFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
		if self.grammar_type == 'split':
			self.parser_grammar += f'parser grammar {self.grammar_name}Parser;\n\noptions {{ tokenVocab={self.grammar_name}Lexer; }}\n'
			self.lexer_grammar += f'lexer grammar {self.grammar_name}Lexer;\n\n'
		else:
			self.parser_grammar += f'grammar {self.grammar_name};\n'

	def exitFormal_syntax(self, ctx:bnfParser.Formal_syntaxContext):
		for rr in self.parser_rules:
			self.parser_grammar += f'\n{rr}\n\t:'
			for aa in self.parser_rules[rr]:
				self.parser_grammar += aa
			self.parser_grammar += '\n\t;\n'
		if self.grammar_type == 'split':
			rule_names = set()
			for tt in self.lexer_tokens:
				rule_name = ''
				for ii, cc in enumerate(tt):
					if cc.isalpha() or (ii != 0 and cc == '_'):
						rule_name += cc.upper()
					elif cc in self.symbols:
						rule_name += self.symbols[cc]
				if rule_name:
					while rule_name in rule_names:
						rule_name += chr(random.randint(ord('A'), ord('Z')))
					self.lexer_grammar += f'{rule_name} : \'{tt}\' ;\n'
					rule_names.add(rule_name)
				else:
					print(f"Warning! Could not create a lexer rule for the token '{tt}'.")

	def exitRule_definition(self, ctx:bnfParser.Rule_definitionContext):
		rule_name = ctx.rule_identifier().getText()
		self.parser_rules[rule_name] = self.rule_tokens
		self.rule_tokens = []

	def exitSeparator(self, ctx:bnfParser.SeparatorContext):
		if not self.alt_stack:
			self.rule_tokens.append('\n')
			self.rule_tokens.append('\t')
		else:
			self.rule_tokens.append(' ')
		self.rule_tokens.append('|')

	def enterOptional_item(self, ctx:bnfParser.Optional_itemContext):
		self.alt_stack.append('[')
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' ')
			self.rule_tokens.append('(')

	def exitOptional_item(self, ctx:bnfParser.Optional_itemContext):
		self.alt_stack.pop()
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' ')
			self.rule_tokens.append(')')
		self.rule_tokens.append('?')

	def enterRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
		self.alt_stack.append('{')
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' ')
			self.rule_tokens.append('(')

	def exitRepeated_item(self, ctx:bnfParser.Repeated_itemContext):
		self.alt_stack.pop()
		left_index, right_index = ctx.getSourceInterval()
		if right_index - left_index > 2:
			self.rule_tokens.append(' ')
			self.rule_tokens.append(')')
		self.rule_tokens.append('*')

	def enterRule_reference(self, ctx:bnfParser.Rule_referenceContext):
		self.rule_tokens.append(' ')
		self.rule_tokens.append(ctx.getText())

	def enterKeyword_or_punctuation(self, ctx:bnfParser.Keyword_or_punctuationContext):
		self.rule_tokens.append(' ')
		self.rule_tokens.append('\'')
		self.rule_tokens.append(ctx.getText())
		self.rule_tokens.append('\'')
		self.lexer_tokens.add(ctx.getText())
