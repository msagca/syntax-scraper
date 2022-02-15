# -*- coding: utf-8 -*-

import antlr4
import argparse
import pdfplumber
import sys
if __name__ is not None and "." in __name__:
	from .bnfLexer import bnfLexer
	from .bnfParser import bnfParser
	from .bnfParserListenerChild import bnfParserListenerChild
else:
	from bnfLexer import bnfLexer
	from bnfParser import bnfParser
	from bnfParserListenerChild import bnfParserListenerChild

def main():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('input_file', help='IEEE language standard (format: PDF)')
	arg_parser.add_argument('-n', required=True, metavar='grammar_name', help='ANTLR4 grammar name')
	arg_parser.add_argument('-s', type=int, required=True, metavar='start_page', help='formal syntax start page')
	arg_parser.add_argument('-e', type=int, required=True, metavar='end_page', help='formal syntax end page')
	arg_parser.add_argument('-f', default='A.1 ', metavar='chapter_text', help='title (or number) of the first chapter (default: A.1 )')
	arg_parser.add_argument('-l', default='A.9.4', metavar='chapter_text', help='title (or number) of the last chapter (default: A.9.4)')
	arg_parser.add_argument('-t', choices=['combined', 'split'], default='combined', metavar='grammar_type', help='ANTLR4 grammar type (default: combined)')
	args = arg_parser.parse_args()
	first_chapter = args.f.lower()
	last_chapter = args.l.lower()
	annex_text = ''
	bold_text = ''
	title_text = ''
	reached_start = False
	reached_end = False
	break_next = False
	with pdfplumber.open(args.input_file) as pdf:
		for nn in range(args.s, args.e+1):
			page = pdf.pages[nn]
			for cc in page.chars:
				cc_text = cc['text']
				cc_font = cc['fontname']
				if cc_font in ('BHDEOM+Arial-BoldMT', 'LHFBEG+Arial,Bold'):
					if break_next:
						break
					title_text += cc_text.lower()
				if reached_start:
					if cc_font in ('BHDFJL+TimesNewRomanPSMT', 'LHFBMH+TimesNewRoman') or cc_text.isspace():
						if bold_text:
							annex_text += '\'' + bold_text + '\''
							bold_text = ''
						if not cc['non_stroking_color']:
							annex_text += cc_text
						if reached_end and not break_next and not cc_text.isspace():
							break_next = True
					elif cc_font in ('BVXWSQ+CourierNew,Bold', 'LHFBKG+TimesNewRoman,Bold'):
						if not cc_text.isspace():
							if bold_text in ('[', ']', '(', ')', '{', '}') or cc_text in ('[', ']', '(', ')', '{', '}'):
								if bold_text:
									annex_text += '\'' + bold_text + '\''
									bold_text = ''
							if cc_text in ('\'', '\\'):
								bold_text += '\\'
							bold_text += cc_text
						elif bold_text:
							annex_text += '\'' + bold_text + '\''
							bold_text = ''
						if reached_end and not break_next:
							break_next = True
				elif title_text.find(first_chapter) != -1:
					reached_start = True
				if not reached_end:
					if title_text.find(last_chapter) != -1:
						reached_end = True
			if reached_end:
				break
	if annex_text:
		input_stream = antlr4.InputStream(annex_text)
		lexer_obj = bnfLexer(input_stream)
		token_stream = antlr4.CommonTokenStream(lexer_obj)
		parser_obj = bnfParser(token_stream)
		tree_obj = parser_obj.formal_syntax()
		listener_obj = bnfParserListenerChild(grammar_name=args.n, grammar_type=args.t)
		walker_obj = antlr4.ParseTreeWalker();
		walker_obj.walk(listener_obj, tree_obj)
		if args.t == 'split':
			fp = open(f'{args.n}Parser.g4', 'w')
			fp.write(listener_obj.parser_grammar)
			fp.close()
			fp = open(f'{args.n}Lexer.g4', 'w')
			fp.write(listener_obj.lexer_grammar)
			fp.close()
		else:
			fp = open(f'{args.n}.g4', 'w')
			fp.write(listener_obj.parser_grammar)
			fp.close()
	else:
		print(f'Error! Could not find the chapter \'{args.f}\'.')
		sys.exit()

if __name__ == '__main__':
	main()
