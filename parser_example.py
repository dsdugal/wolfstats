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


"""
    round_id : int
        The attribute used to distinguish between attack and defence in stopwatch rounds.
    start_time : int
        The time in seconds that this round started (UNIX).
    end_time : int
        The time in seconds that this round ended (UNIX).
    time_limit : int
        The maximum duration in seconds of this round.
"""

### aliases and classes not accounted for in helper classes?