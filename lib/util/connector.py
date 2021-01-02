"""
x
"""

# Global Imports

from pymongo import MongoClient


# Constants

DEFAULT_NAME = "database"
PROTOCOL = "mongodb"

from lib.match import Match


class Connector( object ):
    """
    x
    """

    def __init__( self, address: str, port: int ):
        host = f"{PROTOCOL}://{address}:{port}/"
        self.client = MongoClient( host )
        self.database = self.client[DEFAULT_NAME]
        self.events = self.database['events']
        self.history = self.database['history']
        self.sessions = self.database['sessions']
        self.matches = self.database['matches']
        self.rounds = self.database['rounds']
        self.teams = self.database['teams']
        self.players = self.database['players']
        self.stats = self.database['stats']
        self.wstats = self.database['wstats']


    def get_all( self ) -> list:
        sessions = []
        pass
        return sessions


    def get_ranked( self ) -> list:
        sessions = []
        pass
        return sessions


    def get_unranked( self ) -> list:
        sessions = []
        pass
        return sessions
