parser grammar bnfParser;
options {
	tokenVocab = bnfLexer;
}
formal_syntax: ( rule_definition | ~'::=')*? EOF;
rule_definition: rule_identifier '::=' rule_alternatives;
rule_alternatives: alternative ( '|' alternative)*;
alternative: item+;
item:
	rule_reference
	| keyword_or_punctuation
	| optional_item
	| repeated_item;
optional_item: '[' rule_alternatives ']';
repeated_item: '{' rule_alternatives '}';
rule_identifier: IDENTIFIER;
rule_reference: IDENTIFIER;
keyword_or_punctuation: STRING_TEXT;
