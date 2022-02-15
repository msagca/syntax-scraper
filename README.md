# Syntax Scraper

Convert `Formal Syntax` section of an IEEE language standard document to an [ANTLR4](https://www.antlr.org/) grammar

## Installation

First, generate the BNF parser
```bash
bash ieee/gen_parser.sh
```
Then, install the Python package
```bash
python3 setup.py install --user
```
or
```bash
pip3 install .
```

## Usage

```bash
usage: scrape-ieee [-h] -s start_page -e end_page -n grammar_name [-t grammar_type] input_file

positional arguments:
  input_file       IEEE language standard document (format: PDF)

options:
  -h, --help       show this help message and exit
  -s start_page    formal syntax start page
  -e end_page      formal syntax end page
  -n grammar_name  ANTLR4 grammar name
  -t grammar_type  ANTLR4 grammar type (default: combined)
```

## Example

```bash
scrape-ieee -s 1136 -e 1179 -n SystemVerilog -t split 1800-2017.pdf
```

The tool has been tested on [IEEE Std 1800-2017](https://ieeexplore.ieee.org/document/8299595) and [IEEE Std 1364-2005](https://ieeexplore.ieee.org/document/1620780)  
The resulting grammar requires some extra work:
- Open the created `.g4` file(s) in [Visual Studio Code](https://code.visualstudio.com/)
- Install the [ANTLR4 extension](https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4)
- Manually fix the highlighted issues
