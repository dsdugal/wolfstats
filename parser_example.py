"""
x
"""

# Local Imports

from lib.classes.match import Match
from lib.parsers.parser import Parser


# Driver

parser = Parser()
match_pairs = parser.get_pairs()
for pair in match_pairs:
    match = parser.parse( pair )
    print( match )
