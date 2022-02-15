# -*- coding: utf-8 -*-

import antlr4
import argparse
import pdfplumber
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
	arg_parser.add_argument('input', help='IEEE Std 1364/1800-xxxx PDF')
	arg_parser.add_argument('-n', required=True, metavar='grammar_name', help='Grammar name')
	arg_parser.add_argument('-s', type=int, required=True, metavar='start_page', help='Annex A start page')
	arg_parser.add_argument('-e', type=int, required=True, metavar='end_page', help='Annex A end page')
	args = arg_parser.parse_args()
	annex_text = ''
	bold_text = ''
	temp_text = ''
	reached_start = False
	reached_end = False
	with pdfplumber.open(args.input) as pdf:
		for nn in range(args.s, args.e+1):
			page = pdf.pages[nn]
			for cc in page.chars:
				if temp_text.find('Footnotes') != -1:
					reached_end = True
					break
				if reached_start:
					if cc['fontname'] == 'BHDFJL+TimesNewRomanPSMT':
						if bold_text:
							annex_text += '\'' + bold_text + '\''
							bold_text = ''
						if not cc['non_stroking_color']:
							annex_text += cc['text']
					elif cc['fontname'] == 'BVXWSQ+CourierNew,Bold':
						if not cc['text'].isspace():
							if bold_text in ('[', ']', '(', ')', '{', '}') or cc['text'] in ('[', ']', '(', ')', '{', '}'):
								if bold_text:
									annex_text += '\'' + bold_text + '\''
									bold_text = ''
							if cc['text'] in ('\'', '\\'):
								bold_text += '\\'
							bold_text += cc['text']
						elif bold_text:
							annex_text += '\'' + bold_text + '\''
							bold_text = ''
				elif temp_text.find('Source text') != -1:
					reached_start = True
				if cc['fontname'] == 'BHDEOM+Arial-BoldMT':
					temp_text += cc['text']
			if reached_end:
				break
	input_stream = antlr4.InputStream(annex_text)
	lexer_obj = bnfLexer(input_stream)
	token_stream = antlr4.CommonTokenStream(lexer_obj)
	#token_stream.fill()
	#for tt in token_stream.tokens:
	#	print(tt)
	parser_obj = bnfParser(token_stream)
	tree_obj = parser_obj.formal_syntax()
	listener_obj = bnfParserListenerChild(name=args.n)
	walker_obj = antlr4.ParseTreeWalker();
	walker_obj.walk(listener_obj, tree_obj)
	if listener_obj.grammar_definition:
		fp = open(f'{args.n}.g4', 'w')
		fp.write(listener_obj.grammar_definition)
		fp.close()

if __name__ == '__main__':
	main()
