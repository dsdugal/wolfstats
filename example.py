"""
x
"""

# Local Imports

from lib.stat.apm import APM
from lib.util.connector import Connector
from lib.util.parser import Parser


# Driver

connector = Connector( "localhost" ) # instantiate the database interface object
parser = Parser() # instantiate the class constructor object
system = APM( connector ) # instantiate the rating system
sessions = parser.get_unranked() # retrieve all matches in the database not yet ranked
system.rank( sessions ) # retrieve all player ranks, process sessions, update player ranks