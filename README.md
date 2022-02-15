# Syntax Scraper

Convert `Formal Syntax` section of an IEEE language standard document to an [ANTLR4](https://www.antlr.org/) grammar

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
usage: scrape-ieee [-h] -n grammar_name -s start_page -e end_page [-f chapter_text] [-l chapter_text] [-t grammar_type] input_file

positional arguments:
  input_file       IEEE language standard (format: PDF)

options:
  -h, --help       show this help message and exit
  -n grammar_name  ANTLR4 grammar name
  -s start_page    formal syntax start page
  -e end_page      formal syntax end page
  -f chapter_text  title (or number) of the first chapter (default: A.1 )
  -l chapter_text  title (or number) of the last chapter (default: A.9.4)
  -t grammar_type  ANTLR4 grammar type (default: combined)
```

## Example

```bash
scrape-ieee -n SystemVerilog -s 1136 -e 1179 -f 'A.1 ' -l 'A.9.4' -t split 1800-2017.pdf
```

The resulting grammar requires some extra work:
- Open the created `.g4` file(s) in [Visual Studio Code](https://code.visualstudio.com/)
- Install the [ANTLR4 extension](https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4)
- Manually fix the highlighted issues
