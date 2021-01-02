"""
x
"""

# Local Imports

from lib.stat.apm import APM
from lib.util.connector import Connector


# Driver

connector = Connector() # instantiate the database interface object
system = APM( connector ) # instantiate the rating system
matches = connector.get_unranked() # retrieve all matches in the database not yet ranked
system.rank( matches ) # retrieve all player ranks, process matches, update player ranks