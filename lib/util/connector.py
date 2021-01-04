"""
x
"""

# Global Imports

from pymongo import MongoClient


# Local Imports

from lib.match import Match


class Connector( object ):
    """
    x
    """

    def __init__( self, address: str, port: int = 27017 ):
        """
        Parameters
        ----------
        address : str
            The address of a MongoDB database.
        port : int
            The port that the database runs on.
        """

        self.host = f"mongodb://{address}:{port}/"
        self.client = MongoClient( self.host )
