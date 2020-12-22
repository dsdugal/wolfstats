"""
x
"""

# Global Imports

from time import time


# Local Imports

import lib.constants as info


class Round( object ):
    """
    x
    """

    def __init__( self, round_id: int ):
        """
        Parameters
        ----------
        round_id : int
            x
        """

        self._round_id = round_id
        self._start_time = None
        self._end_time = None
        self._time_limit = None
        self._events = []
        self._stats = None
        self._wstats = None


    def __str__( self ):
        string = f"    round_id: {self.round_id}\n"
        string += f"    start_time: {self.start_time}\n"
        string += f"    end_time: {self.end_time}\n"
        string += f"    time_limit: {self.time_limit}\n"
        string += f"    events:\n"
        for event in self.events:
            string += f"        ({event})\n"
        string += f"    stats:\n"
        string += f"    {self.stats}\n"
        string += f"    wstats:\n"
        string += f"    {self.wstats}\n"
        return string


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


    @round_id.setter
    def round_id( self, round_id : int ):
        assert round_id in info.ROUNDS
        self._round_id = round_id


    @property
    def start_time( self ) -> int:
        return self._start_time


    @start_time.setter
    def start_time( self, start_time : int ):
        self._validate_times( start_time, self.end_time )
        self._start_time = start_time


    @property
    def end_time( self ) -> int:
        return self._end_time


    @end_time.setter
    def end_time( self, end_time : int ):
        self._validate_times( self.start_time, end_time )
        self._end_time = end_time


    @property
    def time_limit( self ) -> int:
        return self._time_limit


    @time_limit.setter
    def time_limit( self, time_limit : int ):
        assert time_limit >= ( self.end_time - self.start_time )
        self._time_limit = time_limit


    @property
    def events( self ) -> list:
        return self._events


    @events.setter
    def events( self, events: list ):
        assert events
        self._events = events


    @property
    def stats( self ) -> list:
        return self._stats


    @stats.setter
    def stats( self, stats: list ):
        self._stats = stats


    @property
    def wstats( self ) -> list:
        return self._wstats


    @wstats.setter
    def wstats( self, wstats: list ):
        self._wstats = wstats


    # Derivatives

    @property
    def inactive_periods( self ) -> list:
        """
        Returns a list of time periods during which the round was paused.
        """

        periods = []
        for event in self.events:
            if event.label == "pause":
                start_time = event.time
            elif event.label == "unpause":
                end_time = event.time
                periods.append([start_time, end_time])
        return periods


    @property
    def length( self ) -> int:
        """
        Returns the total active time of this round.
        """

        length = 0
        if self.events:
            duration = self.end_time - self.start_time
            length = duration - len( self.inactive_periods )
        return length


    @property
    def players( self ) -> list:
        """
        Returns the list of players in this round.
        """

        if self.stats:
            return self.stats.column_data( 0 )
        return 0


    @property
    def size( self ):
        """
        Returns the number of players in this round
        """

        if self.stats:
            return len( self.stats.body )
        return 0


    # Input Validation

    def _validate_times( self, start_time: int, end_time: int ):
        """
        x

        Parameters
        ----------
        start_time : int
            x
        end_time : int
            x
        """
        
        if start_time:
            assert time() > start_time > 0
        if end_time:
            assert time() > end_time > 0
        if start_time and end_time:
            assert end_time > start_time


    # Public Methods

    def team( self, team_name: str ) -> list:
        """
        Returns a list of players on the specified team in this round.

        Parameters
        ----------
        team_name : str
            The proper name of the team.
        """

        assert team_name in info.TEAMS.values()
        players = []
        if self.stats:
            players.extend( self.stats.column_data( 0, 1, "allies" ))
        return players


    def team_size( self, team_name: str ) -> list:
        """
        Returns the number of players on specified team in this round.

        Parameters
        ----------
        team_name : str
            The proper name of the team.
        """

        assert team_name in info.TEAMS.values()
        return len( self.team( team_name ))
