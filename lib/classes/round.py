"""
x
"""

# Local Imports

import lib.constants as info


class Round( object ):
    """
    Parameters
    ----------
    match_id : int
        x
    """

    def __init__( self, match_id: int ):
        assert match_id > 0
        self._match_id = match_id
        self._round_id = None
        self._start_time = None
        self._end_time = None
        self._time_limit = None
        self._events = None


    def __str__( self ):
        pass


    # Properties

    @property
    def match_id( self ) -> int:
        return self._match_id


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


    # Derivatives

    @property
    def duration( self ) -> int:
        return self.end_time - self.start_time


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


    # Input Validation

    def _validate_times( self, start_time: int, end_time: int ):
        if start_time:
            assert start_time > 0
        if end_time:
            assert end_time > 0
        if start_time and end_time:
            assert start_time > end_time
