#!/usr/bin/bash

ANTLR4_VERSION='4.10'
ANTLR4_JAR=antlr-$ANTLR4_VERSION-complete.jar
ANTLR4_PATH="/usr/local/lib/$ANTLR4_JAR"
ANTLR4="java -jar $ANTLR4_PATH"

if [ ! -f "$ANTLR4_PATH" ]; then
	(cd /usr/local/lib && sudo curl -O https://www.antlr.org/download/"$ANTLR4_JAR")
fi

cd "$(dirname "$0")"
$ANTLR4 -Dlanguage=Python3 bnfLexer.g4
$ANTLR4 -Dlanguage=Python3 bnfParser.g4
