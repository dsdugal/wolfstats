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


# Constants

SUPPORTED_FORMAT = "json"
SUPPORTED_SCHEMAS = [
    0.1
]


class Parser( object ):
    """
    x
    """

    # Private Methods

    def _parse_match( self, data: dict ) -> Match:
        """
        Returns a Match object that contains match summary information.

        Parameters
        ----------
        data : dict
            The data from a valid JSON file.
        """

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
        return match


    def _parse_round( self, match: Match, data: dict ) -> Match:
        """
        Updates and returns a Match object with round information.

        Parameters
        ----------
        match : Match
            x
        data : dict
            The data from a valid JSON file.
        """

        branch = data['round']
        instance = Round( branch['round_id'] )
        instance.start_time = branch['start_time']
        instance.end_time = branch['end_time']
        instance.time_limit = branch['time_limit']
        for context in branch['events']:
            time = context.pop( 'time' )
            instance.events.append( Event( time, context ))
        match.rounds.append( instance )
        return match


    def _parse_stat( self, match: Match, data: dict ) -> Match:
        """
        Updates and returns a Match object with player stat information.

        Parameters
        ----------
        match : Match
            x
        data : dict
            The data from a valid JSON file.
        """

        branch = data['stats']
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
            # break
        match.stats.append( Table( headers, body ))
        return match


    def _parse_wstat( self, match: Match, data: dict ) -> Match:
        """
        Updates and returns a Match object with player wstat information.

        Parameters
        ----------
        match : Match
            x
        data : dict
            The data from a valid JSON file.
        """

        branch = data['wstats']
        headers = list( info.DEFAULT_HEADERS )[0:2]
        headers.extend( info.WSTAT_HEADERS )
        body = []
        for guid in branch:
            for wstat in branch[guid]:
                stat_line = [guid]
                stat_line.extend( list( wstat.values()))
                body.append( stat_line )
            # break
        match.wstats.append( Table( headers, body ))
        return match

    
    # Input Validation

    def _validate_path( self, file_path: str ) -> dict:
        """
        Validates the path of a file and returns the data if it is in a supported format.

        Parameters
        ----------
        file_path : str
            The relative path of a JSON file.
        """

        assert 0 < len( file_path ) < 256
        try:
            with open( file_path, "r" ) as data_file:
                data = loads( data_file.read())
                schema = data['schema']
                assert schema in SUPPORTED_SCHEMAS
        except FileNotFoundError:
            pass
            exit( False )
        return data


    # Public Methods

    def get_pairs( self, directory: str = "data" ) -> list:
        """
        Returns a list of JSON file paths
        """

        pairs = []
        files = sorted( glob( f"{directory}/*.{SUPPORTED_FORMAT}" ))
        for file in reversed( files ):
            match_id = search( r"\d{10}", file )
            if not match_id:
                files.pop( files.index( file ))
        i = -1
        previous_id = None
        for file in files:
            matcher = search( r"\d{10}", file )
            if matcher:
                current_id = matcher.group( 0 )
                if current_id == previous_id:
                    pairs[i].append( file )
                else:
                    i += 1
                    pairs.insert( i, [file])

            previous_id = current_id
        return pairs


    def parse( self, file_paths: list ) -> Match:
        """
        x
        """

        valid_data = []
        for file_path in file_paths:
            valid_data.append( self._validate_path( file_path ))
        match = self._parse_match( valid_data[0] )
        for data in valid_data:
            match = self._parse_round( match, data )
            match = self._parse_stat( match, data )
            match = self._parse_wstat( match, data )
        return match


    def parse_match( self, file_path: str ) -> Match:
        """
        x
        """
        
        data = self._validate_path( file_path )
        match = self._parse_match( data )
        match.winner = data['summary']['winner']
        return match


    def parse_round( self, file_paths: list ) -> Match:
        """
        x
        """
        
        valid_data = []
        for file_path in file_paths:
            valid_data.append( self._validate_path( file_path ))
        match = self._parse_match( valid_data[0] )
        for data in valid_data:
            match = self._parse_round( match, data )
        if not match.winner:
            match.winner = valid_data[-1]['summary']['winner']
        return match


    def parse_stat( self, file_paths: list ) -> Match:
        """
        x
        """
        

        valid_data = []
        for file_path in file_paths:
            valid_data.append( self._validate_path( file_path ))
        match = self._parse_match( valid_data[0] )
        for data in valid_data:
            match = self._parse_stat( match, data )
        if not match.winner:
            match.winner = valid_data[-1]['summary']['winner']
        return match


    def parse_wstat( self, file_paths: list ) -> Match:
        """
        x
        """
        
        valid_data = []
        for file_path in file_paths:
            valid_data.append( self._validate_path( file_path ))
        match = self._parse_match( valid_data[0] )
        for data in valid_data:
            match = self._parse_wstat( match, data )
        if not match.winner:
            match.winner = valid_data[-1]['summary']['winner']
        return match
