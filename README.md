# Syntax Scraper

## Installation

First, generate the BNF parser
```bash
bash ieee/gen_parser.sh
```
then, install the package
```bash
python3 setup.py install --user
```
or
```bash
pip3 install .
```

## Usage

```bash
scrape-ieee 1800-2017.pdf -s 1136 -e 1179 -n SystemVerilog
```
