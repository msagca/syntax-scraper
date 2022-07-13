#!/usr/bin/bash

ANTLR4_VERSION='4.10'
ANTLR4_JAR=antlr-$ANTLR4_VERSION-complete.jar
ANTLR4_PATH=/usr/local/lib/$ANTLR4_JAR
ANTLR4="java -jar $ANTLR4_PATH"

if [ ! -f "$ANTLR4_PATH" ]; then
	sudo curl -L https://www.antlr.org/download/"$ANTLR4_JAR" -o /usr/local/lib
fi

cd "$(dirname "$0")"
$ANTLR4 -Dlanguage=Python3 bnfLexer.g4
$ANTLR4 -Dlanguage=Python3 -visitor -no-listener bnfParser.g4
