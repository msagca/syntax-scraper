# -*- coding: utf-8 -*-

import antlr4
import argparse
import pdfplumber
if __name__ is not None and "." in __name__:
	from .bnfLexer import bnfLexer
	from .bnfParser import bnfParser
	from .Scraper import Scraper
else:
	from bnfLexer import bnfLexer
	from bnfParser import bnfParser
	from Scraper import Scraper

def main():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('input_file', help='IEEE language standard document (format: PDF)')
	arg_parser.add_argument('-n', required=True, metavar='grammar_name', help='ANTLR4 grammar name')
	arg_parser.add_argument('-s', type=int, metavar='start_page', help='formal syntax start page (default: first page)')
	arg_parser.add_argument('-e', type=int, metavar='end_page', help='formal syntax end page (default: last page)')
	args = arg_parser.parse_args()
	syntax_text = ''
	with pdfplumber.open(args.input_file) as pdf:
		bold_text = ''
		start_page = args.s if args.s else 1
		end_page = args.e if args.e else len(pdf.pages)
		for pp in range(start_page, end_page):
			page = pdf.pages[pp]
			for char in page.chars:
				char_text = char['text']
				char_font = char['fontname'].lower()
				if char_text == '\\':
					char_text = '\\' + char_text
				elif char_text == "'":
					char_text = '\\' + char_text
					if 'bold' not in char_font:
						char_text = "'" + char_text + "'"
				if char_text.isspace() or char_text == '§' or 'bold' not in char_font:
					if bold_text:
						syntax_text += "'" + bold_text + "'"
						bold_text = ''
					syntax_text += char_text
				else:
					bold_text += char_text
	input_stream = antlr4.InputStream(syntax_text)
	lexer = bnfLexer(input_stream)
	token_stream = antlr4.CommonTokenStream(lexer)
	parser = bnfParser(token_stream)
	tree = parser.formal_syntax()
	visitor = Scraper()
	grammar_text = f'grammar {args.n};'
	grammar_text += visitor.visit(tree)
	with open(f'{args.n}.g4', 'w') as fp:
		fp.write(grammar_text)

if __name__ == '__main__':
	main()
