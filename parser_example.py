"""
x
"""

# Global Imports

from glob import glob
from json import dumps, loads


# Local Imports

import lib.constants as info
from lib.classes.match import Match
from lib.parsers.parser import Parser


# Driver

data_files = glob( "data/*.json" )

if data_files:
    for data_file in data_files:
        parser = Parser()
        match = parser.parse( [data_file] )
        print( match )
else:
    exit( True )
    