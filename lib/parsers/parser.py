"""
x
"""

# Global Imports

from json import loads


# Local Imports

from lib.classes.match import Match
from lib.classes.round import Round
from lib.classes.table import Table
from lib.classes.wstat import WStat
import lib.constants as info


# Constants

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
        x
        """

        instance = Match( data['match_id'] )
        instance.start_time = data['summary']['start_time']
        instance.end_time = data['summary']['end_time']
        instance.host_address = data['summary']['host_address']
        instance.host_port = data['summary']['host_port']
        instance.mod_name = data['summary']['mod_name']
        instance.mod_version = data['summary']['mod_version']
        instance.mod_config = data['summary']['mod_config']
        instance.gametype = data['summary']['gametype']
        instance.mapname = data['summary']['mapname']
        instance.allies_cycle = data['summary']['allies_cycle']
        instance.axis_cycle = data['summary']['axis_cycle']
        instance.winner = data['summary']['winner']
        instance.rounds = []
        if data['stats']:
            headers = info.DEFAULT_HEADERS.keys().extend( info.CATEGORY_HEADERS )
        for element in data['stats']:
            body = []
            for guid in element:
                stat_line = [guid]
                stat_line.append( element[guid]['team'] )
                stat_line.append( element[guid]['start_time'] )
                stat_line.append( element[guid]['end_time'] )
                stat_line.extend( list( element[guid]['categories'].values()))
                body.append( stat_line )
            instance.rounds.append( Table( headers, body ))
        return instance


    def _parse_round( self, data: dict ) -> list:
        """
        x
        """

        instances = []
        for element in data['rounds']:
            instance = Round( data['match_id'] )
            instance.round_id = len( instances ) + 1
            instance.start_time = element['start_time']
            instance.end_time = element['end_time']
            instance.time_limit = element['time_limit']
            instance.events = [ event for event in element['events']]
            instances.append( instance )
        return instances


    def _parse_wstat( self, data: dict ) -> list:
        """
        x
        """

        instances = []
        if data['wstats']:
            headers = list( info.DEFAULT_HEADERS )[0:2].extend( info.WSTAT_HEADERS )
        for element in data['wstats']:
            instance = WStat( data['match_id'] )
            body = []
            for guid in element:
                for wstat in element[guid]:
                    stat_line = [guid]
                    stat_line.extend( list( wstat.values()))
                    body.append( stat_line )
            instance.table = Table( headers, body )
            instances.append( instance )
        return instances

    
    # Input Validation

    def _validate_path( self, file_path: str ) -> dict:
        """
        x
        """

        assert file_path
        assert 0 < len( file_path ) < 256
        with open( file_path, "r" ) as data_file:
            data = loads( data_file.read())
            schema = data['schema']
            assert schema in SUPPORTED_SCHEMAS
            return data


    # Public Methods

    def parse_all( self, file_path: str ) -> tuple:
        """
        x
        """

        data = self._validate_path( file_path )
        match_data = self._parse_match( data )
        round_data = self._parse_round( data )
        wstat_data = self._parse_wstat( data )
        return match_data, round_data, wstat_data


    def parse_match( self, file_path: str ) -> Match:
        """
        x
        """
        
        data = self._validate_path( file_path )
        match_data = self._parse_match( data )
        return match_data


    def parse_round( self, file_path: str ) -> list:
        """
        x
        """
        
        data = self._validate_path( file_path )
        round_data = self._parse_round( data )
        return round_data


    def parse_wstat( self, file_path: str ) -> list:
        """
        x
        """
        
        data = self._validate_path( file_path )
        wstat_data = self._parse_wstat( data )
        return wstat_data
