"""
x
"""

# Local Imports

import lib.constants as info


class Event( object ):
    """
    x
    """

    def __init__( self, time: int, context: dict ):
        """
        Parameters
        ----------
        time : int
            The time that the event occurred.
        context : dict
            The details associated with the event.
        """

        self._time = time
        self._context = context


    def __str__( self ):
        pass


    def __lt__( self, other: object ):
        return self.time < other.time


    def __le__( self, other: object ):
        return self.time <= other.time


    def __eq__( self, other: object ):
        return self.time == other.time


    def __ne__( self, other: object ):
        return self.time != other.time


    def __ge__( self, other: object ):
        return self.time >= other.time


    def __gt__( self, other: object ):
        return self.time > other.time


    # Properties

    @property
    def time( self ) -> int:
        return self._time


    @property
    def context( self ) -> dict:
        return self._context


    @context.setter
    def context( self, context: dict ):
        self._context = context
