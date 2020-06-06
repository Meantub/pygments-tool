import sys
import argparse
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters import SvgFormatter
from pygments.formatters import ImageFormatter
from pygments.lexers import get_lexer_for_filename
from OneDarkProStyle import OneDarkProStyle

parser = argparse.ArgumentParser(description='Processing code into One Dark Pro format')
parser.add_argument('infile', type=str)
parser.add_argument('outfile', type=str)

arguments = parser.parse_args()

lexer = get_lexer_for_filename(arguments.infile)

inputfile = open(arguments.infile, "r")
if inputfile.mode == "r":
    contents = inputfile.read()

outputfile = open(arguments.outfile, "w")
if outputfile.mode == "w":
    highlight(contents, lexer, SvgFormatter(style=OneDarkProStyle,fontfamily="Hack"), outputfile)
