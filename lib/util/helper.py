"""
x
"""

# Local Imports

from lib.table import Table
import lib.constants as info


class Helper( object ):
    """
    x
    """

    def get_events( self, sequence: list ) -> list:
        """
        x

        Parameters
        ----------
        sequence : list
            x
        """

        events = []
        for item in sequence:
            events.extend( item.events )
        return events


    def get_players( self, sequence: list ) -> list:
        """
        x

        Parameters
        ----------
        sequence : list
            x
        """

        players = []
        for item in sequence:
            players.extend( item.players )
        return players


    def get_stats( self, sequence: list ) -> Table:
        """
        x

        Parameters
        ----------
        sequence : list
            x
        """

        body = []
        headers = info.DEFAULT_HEADERS + info.STAT_HEADERS
        for item in sequence:
            body.extend( item.stats.body )
        return Table( headers, body )


    def get_wstats( self, sequence: list ) -> Table:
        """
        x

        Parameters
        ----------
        sequence : list
            x
        """

        body = []
        headers = info.DEFAULT_HEADERS + info.WSTAT_HEADERS
        for item in sequence:
            body.extend( item.wstats.body )
        return Table( headers, body )


    def inactive_periods( self, events: list ) -> list:
        """
        Returns a list of time periods during which the round was paused.
        """

        periods = []
        for event in events:
            if event.context['label'] == "pause":
                start_time = event.time
            elif event.context['label'] == "unpause":
                end_time = event.time
                periods.append([start_time, end_time])
        return periods


    def inactive_time( self, events: list ) -> list:
        """
        Returns the length of time during which the round was paused.
        """

        periods = self.inactive_periods( events )
        time = 0
        for period in periods:
            time += ( period[1] - period[0] )
        return time


    def length( self, events: list ) -> int:
        """
        x

        Parameters
        ----------
        sequence : list
            x
        """

        last = events[-1]
        prev = events[-2]
        if prev.context['label'] == "clock_set":
            return prev.time - self.inactive_time( events )
        else:
            return last.time - self.inactive_time( events )
