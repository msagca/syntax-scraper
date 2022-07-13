# Syntax Scraper

Converts *formal syntax* section of an IEEE language standard document to an [ANTLR4](https://www.antlr.org/) grammar and outputs it as a *.g4* file.

## Installation

```bash
python3 setup.py install --user
```
or
```bash
pip3 install .
```

## Usage

```bash
scrape-ieee [-h] -n grammar_name [-s start_page] [-e end_page] input_file

positional arguments:
  input_file       IEEE language standard document (format: PDF)

options:
  -h, --help       show this help message and exit
  -n grammar_name  ANTLR4 grammar name
  -s start_page    formal syntax start page (default: first page)
  -e end_page      formal syntax end page (default: last page)
```

## Example

```bash
scrape-ieee -n SystemVerilog -s 1136 -e 1180 1800-2017.pdf
```

The resulting grammar requires some additional work:
- Open the created *.g4* file in [Visual Studio Code](https://code.visualstudio.com/).
- Install the [ANTLR4 extension](https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4).
- Fix the highlighted issues.
- Find every occurance of `'Failed to parse!'` and manually write those rules.
- Remove title text, e.g. `'A.8.7' 'Numbers'`, from the rules.
- Append `EOF` to the start rule(s): `library_text` and `source_text`.
- Identify the [lexer rules](https://github.com/antlr/antlr4/blob/master/doc/lexer-rules.md) (identifier, number, whitespace, etc.) and rewrite them.
