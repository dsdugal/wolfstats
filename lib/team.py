"""
x
"""


class Team( object ):
    """
    x
    """

    def __init__( self, session_id: str, match_id: str, round_id: str, name: str, captain: str, players: list ):
        """
        Parameters
        ----------
        session_id : str
            The unique identifier for the session that the team played in.
        match_id : str
            The unique identifier for the match that the team played in.
        round_id : str
            The unique identifier for the round that the team played in.
        name : str
            The proper name of a team.
        captain : str
            The unique identifier for the player that served as the captain of the team.
        players : list
            A list of the unique identifiers for the players of the team.
        """

        self._session_id = session_id
        self._match_id = match_id
        self._round_id = round_id
        self._name = name
        self._captain = captain
        self._players = players


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
    def session_id( self ) -> str:
        return self._match_id


    @property
    def match_id( self ) -> str:
        return self._match_id


    @property
    def round_id( self ) -> str:
        return self._round_id


    @property
    def name( self ) -> str:
        return self._name
    

    @property
    def captain( self ) -> str:
        return self._captain


    @property
    def players( self ) -> list:
        return self._players
