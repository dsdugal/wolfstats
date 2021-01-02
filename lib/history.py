"""
x
"""


class History( object ):
    """
    x
    """

    def __init__( self, start_time: int, sessions: list ):
        """
        Parameters
        ----------
        start_time : int
            x
        sessions: list
            x
        """

        self._start_time = start_time
        self._sessions = sessions


    @property
    def start_time( self ) -> int:
        return self._start_time


    @property
    def sessions( self ) -> list:
        return self._sessions
