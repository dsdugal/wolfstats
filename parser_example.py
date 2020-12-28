"""
x
"""

# Local Imports

from lib.match import Match
from lib.util.parser import Parser


# Driver

parser = Parser()
match_pairs = parser.get_pairs()
for pair in match_pairs:
    print( parser.parse( pair ))
    exit( True )
