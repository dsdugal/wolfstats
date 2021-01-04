"""
x
"""

# Local Imports

from lib.table import Table


class Player( object ):
    """
    x
    """

    def __init__( self, guid: str, rating: int, stats: Table, wstats: Table ):
        """
        Parameters
        ----------
        guid : str
            x
        rank : int
            x
        stats : Table
            x
        stats : Table
            x
        """

        self._guid = guid
        self._rating = rating
        self._stats = stats
        self._wstats = wstats


    def __lt__( self, other: object ):
        return self.rating < other.rating


    def __le__( self, other: object ):
        return self.rating <= other.rating


    def __eq__( self, other: object ):
        return self.rating == other.rating


    def __ne__( self, other: object ):
        return self.rating != other.rating


    def __ge__( self, other: object ):
        return self.rating >= other.rating


    def __gt__( self, other: object ):
        return self.rating > other.rating


    # Properties

    @property
    def guid( self ) -> str:
        return self._guid


    @property
    def rating( self ) -> int:
        return self._rating


    @property
    def stats( self ) -> Table:
        return self._stats


    @property
    def wstats( self ) -> Table:
        return self._wstats
