"""
x
"""


class Round( object ):
    """
    x
    """

    def __init__( self, session_id: str, match_id: str, round_id: str, start_time: int, end_time: int, time_limit: int, events: list, teams: list ):
        """
        Parameters
        ---------
        session_id : str
            x
        match_id : str
            x
        round_id : str
            x
        events : list
            x
        teams : list
            x
        """

        self._session_id = session_id
        self._match_id = match_id
        self._round_id = round_id
        self._start_time = start_time
        self._end_time = end_time
        self._time_limit = time_limit
        self._events = []
        self._teams = []


    def __lt__( self, other: object ):
        return self.round_id < other.round_id


    def __le__( self, other: object ):
        return self.round_id <= other.round_id


    def __eq__( self, other: object ):
        return self.round_id == other.round_id


    def __ne__( self, other: object ):
        return self.round_id != other.round_id


    def __ge__( self, other: object ):
        return self.round_id >= other.round_id


    def __gt__( self, other: object ):
        return self.round_id > other.round_id


    # Properties

    @property
    def session_id( self ) -> int:
        return self._match_id


    @property
    def match_id( self ) -> int:
        return self._match_id


    @property
    def round_id( self ) -> int:
        return self._round_id


    @property
    def start_time( self ) -> int:
        return self._start_time


    @property
    def end_time( self ) -> int:
        return self._end_time


    @property
    def time_limit( self ) -> int:
        return self._time_limit


    @property
    def events( self ) -> list:
        return self._events


    @events.setter
    def events( self, events: list ):
        self._events = events


    @property
    def teams( self ) -> list:
        return self._teams


    @teams.setter
    def teams( self, teams: list ):
        self._teams = teams
