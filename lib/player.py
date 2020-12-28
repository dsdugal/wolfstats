"""
x
"""

# Local Imports

from lib.table import Table
import lib.constants as info


class Player( object ):
    """
    x
    """

    def __init__( self, guid: str ):
        """
        Parameters
        ----------
        guid : str
            The unique identifier for the player.
        """

        self._guid = guid
        self._stats = None
        self._wstats = None


    def __str__( self ):
        pass


    def __lt__( self, other: object ):
        return self.guid < other.guid


    def __le__( self, other: object ):
        return self.guid <= other.guid


    def __eq__( self, other: object ):
        return self.guid == other.guid


    def __ne__( self, other: object ):
        return self.guid != other.guid


    def __ge__( self, other: object ):
        return self.guid >= other.guid


    def __gt__( self, other: object ):
        return self.guid > other.guid


    # Properties

    @property
    def guid( self ) -> str:
        return self._guid


    @property
    def stats( self ) -> Table:
        return self._stats


    @stats.setter
    def stats( self, stats: Table ):
        self._stats = stats


    @property
    def wstats( self ) -> Table:
        return self._wstats


    @wstats.setter
    def wstats( self, wstats: Table ):
        self._wstats = wstats
