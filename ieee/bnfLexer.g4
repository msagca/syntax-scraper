lexer grammar bnfLexer;
IDENTIFIER: [a-z] [a-z_0-9]*;
CAPITALIZED_WORD: [A-Z] ~[ \t\r\n]*;
SECTION_REFERENCE:
	'[' ~('[' | ']')* '§' ~('[' | ']')* ']' -> skip;
DOUBLE_COLON_EQUAL: '::=';
VERTICAL_BAR: '|';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
APOSTROPHE: '\'' -> skip, pushMode(STRING_MODE);
OTHER: . -> skip;
mode STRING_MODE;
STRING_TEXT: ~['\\]+;
STRING_ESC_SEQ: '\\' ( '\'' | '\\') -> type(STRING_TEXT);
STRING_APOSTROPHE: '\'' -> skip, popMode;
STRING_OTHER: . -> skip;
