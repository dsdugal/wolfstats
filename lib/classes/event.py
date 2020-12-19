"""
x
"""

# Local Imports

import lib.constants as info


class Event( object ):
    """
    """

    def __init__( self, time: int, context: dict ):
        """
        Parameters
        ----------
        time : str
            The time that this event occurred.
        context : dict
            The details for this event.
        """

        assert time > 0
        self._time = time
        self._context = context


    def __str__( self ):
        return f"( time: {self.time} => {self.context} )"


    def __lt__( self, other ):
        return self.time < other.time


    def __le__( self, other ):
        return self.time <= other.time


    def __eq__( self, other ):
        return self.time == other.time


    def __ne__( self, other ):
        return self.time != other.time


    def __ge__( self, other ):
        return self.time >= other.time


    def __gt__( self, other ):
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
        assert context
        self._context = context
