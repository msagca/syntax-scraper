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
scrape-ieee [-h] -n grammar_name [-s start_page] [-e end_page] [--split] input_file

positional arguments:
  input_file       IEEE language standard document (format: PDF)

options:
  -h, --help       show this help message and exit
  -n grammar_name  ANTLR4 grammar name
  -s start_page    formal syntax start page (default: first page)
  -e end_page      formal syntax end page (default: last page)
  --split          create a split grammar
```

## Example

```bash
scrape-ieee -n SystemVerilog -s 1136 -e 1180 1800-2017.pdf
```

The resulting grammar requires some additional work:
- Open the created *.g4* file in [Visual Studio Code](https://code.visualstudio.com/).
- Install the [ANTLR4 extension](https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4).
- Fix the highlighted issues.
- Find every occurance of `'Error!'` and manually write those rules.
- Remove title text, e.g. `'A.8.7' 'Numbers'`, from the rules.
- Remove trailing numbers in rule identifiers, e.g. change `time_literal44` to `time_literal`, unless such rule is present in the spec.
- Identify the rules that are spread across multiple pages in the spec and manually add the missing parts if there are any.
- Append `EOF` to the start rule(s): `library_text` and `source_text`.
- Find the rules that describe lexical tokens (white space, comment, identifier, number, etc.) and convert them to [lexer rules](https://github.com/antlr/antlr4/blob/master/doc/lexer-rules.md).

If the `--split` option is specified, the tool will create a lexer rule for every keyword or punctuation symbol it comes across during parse tree walk. It will also create rules for common lexical structures such as identifiers, white spaces and comments, which can be extended later by the user. Due to tool limitations and/or parse errors some of these rules may be invalid or incorrect, e.g. most tokens that begin with a capital letter, and they need to be removed or modified. Also, some symbols that are written in bold in the specification document do not directly translate to lexical tokens and they need to be handled manually. For example, the auto-generated lexer grammar for `SystemVerilog` would contain the rule `LPASRP : '(*)' ;` which does not accept white spaces; however, it is clear that the input `( * )` should also be valid since parentheses act as argument delimiters in this context. Therefore, `LPASRP` needs to be rewritten as three separate rules, e.g. `LP : '(' ;`, `AS : '*' ;` and `RP : ')' ;`, so that the input `(*)` produces three distinct tokens: `(`, `*` and `)`. Similarly, every occurance of this character sequence should be rewritten as `'(' '*' ')'` in the parser grammar.
