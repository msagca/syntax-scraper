#!/usr/bin/bash

if [ $EUID -eq 0 ]; then
	echo "Please run the script without super user privileges." 
	exit
fi

cd "$(dirname "$0")" || exit

ANTLR4_VERSION="4.9.3"
ANTLR4_JAR=antlr-$ANTLR4_VERSION-complete.jar
ANTLR4_JAR_PATH="/usr/local/lib/$ANTLR4_JAR"
ANTLR4="java -jar $ANTLR4_JAR_PATH"

source get_antlr4.sh "$ANTLR4_VERSION"

$ANTLR4 -Dlanguage=Python3 bnfLexer.g4
$ANTLR4 -Dlanguage=Python3 bnfParser.g4
