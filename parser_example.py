"""
An example of how to create Match objects and display their data.

Currently, to run this example:
    - comment out match.py line 28
    - add 'break' after parser.py line 87 and 105 
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
