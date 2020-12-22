"""
x
"""

# Global Imports

from glob import glob
from json import loads
from re import search


# Local Imports

from lib.classes.event import Event
from lib.classes.match import Match
from lib.classes.round import Round
from lib.classes.table import Table
import lib.constants as info


class Parser( object ):
    """
    x
    """

    # Private Methods

    def _parse_summary( self, data: dict, match: Match = None ) -> Match:
        """
        Returns a Match object that contains match summary data.

        Parameters
        ----------
        data : dict
            The raw data from a valid JSON file.
        match: Match
            The data structure that contains relevant match data.
        """

        if not match:
            match = Match( data['match_id'] )
        match.start_time = data['summary']['start_time']
        match.end_time = data['summary']['end_time']
        match.host_address = data['summary']['host_address']
        match.host_port = data['summary']['host_port']
        match.mod_name = data['summary']['mod_name']
        match.mod_version = data['summary']['mod_version']
        match.mod_config = data['summary']['mod_config']
        match.gametype = data['summary']['gametype']
        match.mapname = data['summary']['mapname']
        match.allies_cycle = data['summary']['allies_cycle']
        match.axis_cycle = data['summary']['axis_cycle']
        match.winner = data['summary']['winner']
        return match


    def _parse_round( self, data: dict, match: Match ) -> Match:
        """
        Returns a Match object that contains round specific data.

        Parameters
        ----------
        data : dict
            The raw data from a valid JSON file.
        match: Match
            The data structure that contains relevant match data.
        """

        branch = data['round']
        element = Round( branch['round_id'] )
        element.start_time = branch['start_time']
        element.end_time = branch['end_time']
        element.time_limit = branch['time_limit']
        element = self._parse_events( data, element )
        element = self._parse_stats( data, element )
        element = self._parse_wstats( data, element )
        match.rounds.append( element )
        return match


    def _parse_events( self, data: dict, element: Round ) -> Round:
        """
        Returns a Round object that contains event data.

        Parameters
        ----------
        data : dict
            The raw data from a valid JSON file.
        match: Match
            The data structure that contains relevant round data.
        """

        branch = data['round']['events']
        for context in branch:
            time = context.pop( 'time' )
            element.events.append( Event( time, context ) )
        return element


    def _parse_stats( self, data: dict, element: Round ) -> Round:
        """
        Returns a Round object that contains stats data.

        Parameters
        ----------
        data : dict
            The raw data from a valid JSON file.
        element: Round
            The data structure that contains relevant round data.
        """

        branch = data['round']['stats']
        headers = list( info.DEFAULT_HEADERS.keys())
        headers.extend( info.CATEGORY_HEADERS )
        body = []
        for guid in branch:
            stat_line = [guid]
            stat_line.append( branch[guid]['team'] )
            stat_line.append( branch[guid]['start_time'] )
            stat_line.append( branch[guid]['end_time'] )
            stat_line.extend( list( branch[guid]['categories'].values()))
            body.append( stat_line )
            break ####
        element.stats = Table( headers, body )
        return element


    def _parse_wstats( self, data: dict, element: Round ) -> Round:
        """
        Returns a Round object that contains weapon stats data.

        Parameters
        ----------
        data : dict
            The raw data from a valid JSON file.
        element: Round
            The data structure that contains relevant round data.
        """

        branch = data['round']['wstats']
        headers = list( info.DEFAULT_HEADERS )[0:2]
        headers.extend( info.WSTAT_HEADERS )
        body = []
        for guid in branch:
            for wstat in branch[guid]:
                stat_line = [guid]
                stat_line.extend( list( wstat.values()))
                body.append( stat_line )
            break ####
        element.wstats = Table( headers, body )
        return element


    # Input Validation

    def _validate_paths( self, file_paths: list ) -> list:
        """
        Returns a list of extracted data if the data is in a supported format.

        Parameters
        ----------
        file_paths : list
            The relative paths of the server files to be validated.
        """

        valid_data = []
        for file_path in file_paths:
            try:
                with open( file_path, "r" ) as data_file:
                    data = loads( data_file.read())
                    schema = data['schema']
                    assert schema in info.SUPPORTED_SCHEMAS
                    valid_data.append( data )
            except FileNotFoundError:
                pass
                # log error
        return valid_data


    # Public Methods

    def get_pairs( self, directory: str = "data" ) -> list:
        """
        Returns a list of JSON file pairs, sorted by match_id and round_id.

        Parameters
        ----------
        directory : str
            x
        """

        pairs = {}
        files = sorted( glob( f"{directory}/*.{info.SUPPORTED_FORMAT}" ))
        for file in files:
            matcher = search( r"\d{10}", file )
            if matcher:
                match_id = matcher.group( 0 )
                if match_id in pairs:
                    pairs[match_id].append( file )
                else:
                    pairs[match_id] = [file]
        return list( pairs.values())


    def parse( self, file_paths: list ) -> Match:
        """
        Parses a pair of valid JSON files and returns a Match object that contains all relevant data.
        """

        match = None
        valid_data = self._validate_paths( file_paths )
        for data in valid_data:
            match = self._parse_summary( data, match )
            match = self._parse_round( data, match )
        return match
