"""
x
"""

# Local Imports

from lib.match import Match
from lib.table import Table
from lib.util.helper import Helper


class Session( object ):
    """
    x
    """

    def __init__( self ):
        self._session_id = None # this needs to be unique
        self._start_time = None
        self._end_time = None
        self._matches = []
        self._helper = Helper()


    def __str__( self ):
        string = "\n"
        string += f"session_id: {self._session_id}\n"
        string += f"matches:\n"
        for each in self.matches:
            string += f"{each}\n"
        return string


    @property
    def session_id( self ) -> str:
        return self._session_id


    @property
    def matches( self ) -> list:
        return self._matches


    @matches.setter
    def matches( self, matches: list ):
        self._matches = matches

    
    # Derivatives

    @property
    def events( self ):
        """
        x
        """

        return self._helper.get_events( self.matches )


    @property
    def inactive_periods( self ):
        """
        x
        """

        return self._helper.inactive_periods( self.events )


    @property
    def inactive_time( self ):
        """
        x
        """

        return self._helper.inactive_time( self.events )


    @property
    def length( self ):
        """
        x
        """
        
        return self._helper.length( self.events )


    @property
    def players( self ):
        """
        x
        """

        return list( dict.fromkeys( self._helper.get_players( self.matches )))


    @property
    def size( self ):
        """
        x
        """

        return len( self._helper.get_players( self.matches ))


    @property
    def stats( self ):
        """
        x
        """

        stats = self._helper.get_stats( self.matches )
        stats.combine()
        return stats
    

    @property
    def wstats( self ):
        """
        x
        """

        wstats = self._helper.get_wstats( self.matches )
        wstats.combine()
        return wstats
