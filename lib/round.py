"""
x
"""


# Local Imports
import lib.constants as info


class Round( object ):
    """
    Parameters
    ----------
    round_id : int
        The attribute used to distinguish between attack and defence in stopwatch rounds.
    start_time : int
        The time in seconds that this round started (UNIX).
    end_time : int
        The time in seconds that this round ended (UNIX).
    time_limit : int
        The maximum duration in seconds of this round. 
    """

    def __init__( self, round_id: int, start_time: int, end_time: int, time_limit: int ):
        assert round_id in info.ROUNDS
        assert start_time > 0
        assert end_time > start_time
        assert time_limit >= ( end_time - start_time )
        self._round_id = round_id
        self._start_time = start_time
        self._end_time = end_time
        self._time_limit = time_limit
        self._events = []


    def __str__( self ):
        pass


    # Properties

    @property
    def round_id( self ):
        return self._round_id


    @property
    def start_time( self ):
        return self._start_time


    @property
    def end_time( self ):
        return self._end_time


    @property
    def time_limit( self ):
        return self._time_limit


    @property
    def events( self ):
        return self._events


    @events.setter
    def events( self, events: dict ):
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
