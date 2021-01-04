"""
x
"""


class Match( object ):
    """
    x
    """
    
    def __init__( self, session_id: str, match_id: str, start_time: int, end_time: int, context: dict, rounds: list ):
        """
        Parameters
        ----------
        session_id : str
            x
        match_id : str
            x
        context : dict
            x
        rounds : list
            x
        """

        self._session_id = session_id
        self._match_id = match_id
        self._start_time = start_time
        self._end_time = end_time
        self._context = context
        self._rounds = rounds


    def __lt__( self, other: object ):
        return self.match_id < other.match_id


    def __le__( self, other: object ):
        return self.match_id <= other.match_id


    def __eq__( self, other: object ):
        return self.match_id == other.match_id


    def __ne__( self, other: object ):
        return self.match_id != other.match_id


    def __ge__( self, other: object ):
        return self.match_id >= other.match_id


    def __gt__( self, other: object ):
        return self.match_id > other.match_id


    # Properties

    @property
    def session_id( self ) -> int:
        return self._match_id


    @property
    def match_id( self ) -> int:
        return self._match_id


    @property
    def start_time( self ) -> int:
        return self._start_time


    @property
    def end_time( self ) -> int:
        return self._end_time


    @property
    def context( self ) -> int:
        return self._context


    @property
    def rounds( self ) -> int:
        return self._rounds


    # Derivatives

    @property
    def host_address( self ) -> list:
        return self.context['host_address']


    @property
    def host_port( self ) -> int:
        return self.context['host_port']


    @property
    def mod_name( self ) -> str:
        return self.context['mod_name']


    @property
    def mod_version( self ) -> str:
        return self.context['mod_version']


    @property
    def mod_config( self ) -> str:
        return self.context['mod_config']


    @property
    def gametype( self ) -> int:
        return self.context['gametype']


    @property
    def mapname( self ) -> str:
        return self.context['mapname']


    @property
    def allies_cycle( self ) -> int:
        return self.context['allies_cycle']


    @property
    def axis_cycle( self ) -> int:
        return self.context['axis_cycle']


    @property
    def winner( self ) -> str:
        return self.context['winner']
