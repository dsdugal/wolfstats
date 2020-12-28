"""
x
"""

# Local Imports

from lib.player import Player
from lib.table import Table
from lib.util.helper import Helper
import lib.constants as info


class Team( object ):
    """
    x
    """

    def __init__( self, name: str ):
        """
        Parameters
        ----------
        name : str
            The proper name of the team.
        """

        self._name = name
        self._players = []
        self._helper = Helper()
    

    def __str__( self ):
        string = info.LINE_BREAK * 2
        string += f"name: {self._name}\n"
        for player in self.players:
            string += f"{player}\n"
        return string


    def __lt__( self, other: object ):
        return self.name < other.name


    def __le__( self, other: object ):
        return self.name <= other.name


    def __eq__( self, other: object ):
        return self.name == other.name


    def __ne__( self, other: object ):
        return self.name != other.name


    def __ge__( self, other: object ):
        return self.name >= other.name


    def __gt__( self, other: object ):
        return self.name > other.name


    # Properties

    @property
    def name( self ) -> str:
        return self._name
    

    @property
    def players( self ) -> list:
        return self._players


    @players.setter
    def players( self, players: list ):
        self._players = sorted( players )


    # Derivatives

    @property
    def size( self ) -> int:
        """
        x
        """

        return len( self.players )


    @property
    def stats( self ) -> Table:
        """
        x
        """

        return self._helper.get_stats( self.players )


    @property
    def wstats( self ) -> Table:
        """
        x
        """

        return self._helper.get_wstats( self.players )
