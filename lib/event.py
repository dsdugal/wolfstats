"""
x
"""


class Event( object ):
    """
    x
    """

    def __init__( self, session_id: str, match_id: str, round_id: str, time: int, group: str, context: dict ):
        """
        Parameters
        ----------
        session_id : str
            x
        match_id : str
            x
        round_id : str
            x
        time : int
            x
        group : str
            x
        context : dict
            x
        """

        self._session_id = session_id
        self._match_id = match_id
        self._round_id = round_id
        self._time = time
        self._group = group
        self._context = context


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
    def session_id( self ) -> str:
        return self._match_id


    @property
    def match_id( self ) -> str:
        return self._match_id


    @property
    def round_id( self ) -> str:
        return self._round_id


    @property
    def time( self ) -> int:
        return self._time


    @property
    def group( self ) -> str:
        return self._time


    @property
    def context( self ) -> dict:
        return self._context
