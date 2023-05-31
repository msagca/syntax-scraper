#!/usr/bin/bash

ANTLR4_VERSION='4.13.0'
ANTLR4_JAR=antlr-$ANTLR4_VERSION-complete.jar
ANTLR4_PATH=$HOME/.local/bin/$ANTLR4_JAR
ANTLR4="java -jar $ANTLR4_PATH"

if [ ! -f "$ANTLR4_PATH" ]; then
	curl --create-dirs -L https://www.antlr.org/download/"$ANTLR4_JAR" -o "$ANTLR4_PATH"
fi

cd "$(dirname "$0")"
$ANTLR4 -Dlanguage=Python3 bnfLexer.g4
$ANTLR4 -Dlanguage=Python3 -visitor -no-listener bnfParser.g4
