"""
x
"""

# Local Imports

from lib.team import Team
from lib.table import Table
from lib.util.helper import Helper
import lib.constants as info


class Round( object ):
    """
    x
    """

    def __init__( self, round_id: int ):
        """
        Parameters
        ---------
        round_id : int
            The sequence identifier for the round.
        """

        self._round_id = round_id
        self._start_time = None
        self._end_time = None
        self._time_limit = None
        self._teams = []
        self._events = []
        self._helper = Helper()


    def __str__( self ):
        pass


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
    def round_id( self ) -> int:
        return self._round_id


    @property
    def start_time( self ) -> int:
        return self._start_time


    @start_time.setter
    def start_time( self, start_time : int ):
        self._start_time = start_time


    @property
    def end_time( self ) -> int:
        return self._end_time


    @end_time.setter
    def end_time( self, end_time : int ):
        self._end_time = end_time


    @property
    def time_limit( self ) -> int:
        return self._time_limit


    @time_limit.setter
    def time_limit( self, time_limit : int ):
        self._time_limit = time_limit


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
        self._teams = sorted( teams )


    # Derivatives

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

        return self._helper.get_players( self.teams )


    @property
    def size( self ):
        """
        x
        """

        return len( self._helper.get_players( self.teams ))


    @property
    def stats( self ):
        """
        x
        """

        return self._helper.get_stats( self.teams )
    

    @property
    def wstats( self ):
        """
        x
        """

        return self._helper.get_wstats( self.teams )
