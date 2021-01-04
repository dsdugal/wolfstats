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
sessions = parser.get_unrated() # retrieve all sessions from the database not yet rated
system.rate( sessions ) # retrieve all player ratings, process sessions, update player ratings