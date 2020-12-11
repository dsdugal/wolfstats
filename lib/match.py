# stats: list (only care about rnd ?)

"""
"""

# Global Imports
from time import time

# Local Imports
import lib.constants as constants


class Match( object ):
    """
    """

    def __init__( self, match_id: int, winner: str ):
        """
        """
        self._match_id = match_id
        self._start_time = None
        self._end_time = None
        self._host_address = None
        self._host_port = None
        self._mod_name = None
        self._mod_version = None
        self._gametype = None
        self._mapname = None
        self._allies_cycle = None
        self._axis_cycle = None
        self._winner = winner
        #
        self._stats = None

    def __str__( self ):
        pass


    # Properties

    @property
    def match_id( self ) -> int:
        return self._match_id

    @property
    def start_time( self ) -> int:
        return self._start_time

    @start_time.setter
    def start_time( self, start_time: int ):
        min_time = 0
        max_time = self.end_time if self.end_time else time()
        assert min_time < start_time < max_time
        self._start_time = start_time

    @property
    def end_time( self ) -> int:
        return self._end_time

    @end_time.setter
    def end_time( self, end_time: int ):
        min_time = self.start_time if self.start_time else 0
        max_time = time()
        assert min_time < end_time < max_time
        self._end_time = end_time

    @property
    def host_address( self ) -> list:
        return self._host_address

    @host_address.setter
    def host_address( self, host_address: list ):
        assert len( host_address ) == 4
        assert all( isinstance( v, int ) for v in host_address )
        assert all( 0 <= v <= 255 for v in host_address )
        self._host_address = host_address

    @property
    def host_port( self ) -> int:
        return self._host_port

    @host_port.setter
    def host_port( self, host_port: int ):
        assert 0 < host_port < 65535
        self._host_port = host_port

    @property
    def mod_version( self ) -> str:
        return self._mod_version

    @mod_version.setter
    def mod_version( self, mod_version: str ):
        assert 0 < len( mod_version ) < 64
        self._mod_version = mod_version

    @property
    def gametype( self ) -> int:
        return self._gametype

    @gametype.setter
    def gametype( self, gametype: int ):
        assert gametype in constants.GAMETYPES
        self._gametype = gametype

    @property
    def mapname( self ) -> str:
        return self._mapname

    @mapname.setter
    def mapname( self, mapname: str ):
        assert 0 < len( mapname ) < 64
        self._mapname = mapname

    @property
    def allies_cycle( self ) -> int:
        return self._allies_cycle

    @allies_cycle.setter
    def allies_cycle( self, allies_cycle: int ):
        assert 1 < allies_cycle < 60
        self._allies_cycle = allies_cycle

    @property
    def axis_cycle( self ) -> int:
        return self._axis_cycle

    @axis_cycle.setter
    def axis_cycle( self, axis_cycle: int ):
        assert 1 < axis_cycle < 60
        self._axis_cycle = axis_cycle

    @property
    def winner( self ) -> str:
        return self._winner

    @winner.setter
    def winner( self, winner: str ):
        assert winner in constants.TEAMS
        self._winner = winner

    @property
    def stats( self ) -> list:
        return self._stats

    @stats.setter
    def stats( self, stats: list ):
        self._stats = stats


    # Derivatives

    def allies_players( self ):
        assert self.stats
        ######## TO BE IMPLEMENTED
        return ######## TO BE IMPLEMENTED

    def allies_size( self ):
        assert self.stats
        ######## TO BE IMPLEMENTED
        return ######## TO BE IMPLEMENTED

    def axis_players( self ):
        assert self.stats
        ######## TO BE IMPLEMENTED
        return ######## TO BE IMPLEMENTED

    def axis_size( self ):
        assert self.stats
        ######## TO BE IMPLEMENTED
        return ######## TO BE IMPLEMENTED

    def categories( self ):
        assert self.stats
        ######## TO BE IMPLEMENTED
        return ######## TO BE IMPLEMENTED

    def gametype_str( self ) -> str:
        assert self.gametype
        return constants.GAMETYPES[self.gametype]

    def host_address_str( self ) -> str:
        assert self.host_address and self.host_port
        return ".".join( [f"{str( v )}" for v in self.host_address] ) + f":{str( self.host_port )}"

    def match_size( self ):
        assert self.stats
        return len( self.stats ) - 2

    def match_time( self ) -> int:
        assert self.end_time > self.start_time
        return self.end_time - self.start_time
