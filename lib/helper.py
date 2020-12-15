"""
x
"""

# Local Imports
from lib.event import Event
from lib.match import Match
from lib.round import Round
from lib.table import Table


class Helper( object ):
    """
    x
    """

    def concurrent_kills( self, round: Round ):
        """
        x
        """

        pass


    def consecutive_kills( self ):
        """
        x
        """

        pass


    def filter_events( self, item: Round, time: int, context: dict ) -> list:
        """
        Returns the subset of a round's events that match the specified context.

        Parameters
        ----------
        item : Round
            x
        time : int
            x
        context : dict
            x
        """

        if time:
            return [event for event in item.events if ( event.time == time and event.context.items() >= context.items())]
        else:
            return [event for event in item.events if event.context.items() >= context.items()]


    def clock_time( self, item: Round, time: int ) -> str:
        """
        Returns the time remaining on the round clock at a specified time.
        """

        pass
    

    def inactive_time( self, item: Round, time: int ) -> int:
        """
        Returns the duration in seconds that the round was paused before a specified time.

        x
        """

        return sum( [( period[1] - period[0] ) for period in item.inactive_periods if period[1] < time] )