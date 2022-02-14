#!/usr/bin/bash

if [ $EUID -eq 0 ]; then
	echo "Please run the script without super user privileges." 
	exit
fi

if [ -z "$ANTLR4_VERSION" ]; then
	if [ -z "$1" ]; then
		ANTLR4_VERSION="4.9.3"
	else
		ANTLR4_VERSION="$1"
	fi
fi

if [ -z "$ANTLR4_JAR_PATH" ]; then
	ANTLR4_JAR_PATH="/usr/local/lib/antlr-$ANTLR4_VERSION-complete.jar"
fi

if [ ! -f "$ANTLR4_JAR_PATH" ]; then
	cd /usr/local/lib || exit
	sudo curl -O https://www.antlr.org/download/antlr-"$ANTLR4_VERSION"-complete.jar
	if [ $? != 0 ]; then
		echo "Failed to download ANTLR4 Java binary."
		exit
	fi
fi

if [ ! "$(command -v pip3 2>/dev/null)" ] || [ ! "$(command -v make 2>/dev/null)" ] || [ ! "$(command -v cmake 2>/dev/null)" ] || [ ! "$(command -v g++ 2>/dev/null)" ]; then
	if [ "$(command -v apt 2>/dev/null)" ]; then
		sudo apt install python3-pip make cmake g++ || exit
	elif [ "$(command -v dnf 2>/dev/null)" ]; then
		sudo dnf install python3-pip make cmake g++ || exit
	elif [ "$(command -v yum 2>/dev/null)" ]; then
		sudo yum install python3-pip make cmake g++ || exit
	else
		echo "Could not find a suitable package manager."
		exit
	fi
fi

if [ ! "$(pip3 list | grep antlr4-python3-runtime)" ] || [ "$(pip3 show antlr4-python3-runtime | grep Version | cut -d ' ' -f 2)" != "$ANTLR4_VERSION" ]; then
	pip3 install antlr4-python3-runtime=="$ANTLR4_VERSION"
fi
