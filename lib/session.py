"""
x
"""


class Session( object ):
    """
    x
    """

    def __init__( self, session_id: str, credited: int, ranked: int, matches: list ):
        """
        Parameters
        ----------
        session_id : str
            x
        credited: int
            x
        ranked: int
            x
        matches: list
            x
        """

        self._session_id = session_id
        self._credited = credited
        self._ranked = ranked
        self._matches = matches


    def __lt__( self, other: object ):
        return self.session_id < other.session_id


    def __le__( self, other: object ):
        return self.session_id <= other.session_id


    def __eq__( self, other: object ):
        return self.session_id == other.session_id


    def __ne__( self, other: object ):
        return self.session_id != other.session_id


    def __ge__( self, other: object ):
        return self.session_id >= other.session_id


    def __gt__( self, other: object ):
        return self.session_id > other.session_id


    # Properties

    @property
    def session_id( self ) -> str:
        return self._session_id


    @property
    def credited( self ) -> int:
        return self._session_id


    @credited.setter
    def credited( self, credited: int ):
        self._credited = credited


    @property
    def ranked( self ) -> str:
        return self._ranked


    @ranked.setter
    def ranked( self, ranked: int ):
        self._ranked = ranked


    @property
    def matches( self ) -> list:
        return self._matches
