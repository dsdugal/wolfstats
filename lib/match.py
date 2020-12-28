"""
x
"""

# Local Imports

from lib.round import Round
from lib.table import Table
from lib.util.helper import Helper
import lib.constants as info


class Match( object ):
    """
    x
    """
    
    def __init__( self, match_id: int):
        """
        Parameters
        ----------
        match_id : int
            The unique identifier for the match.
        """

        self._match_id = match_id
        self._start_time = None
        self._end_time = None
        self._host_address = None
        self._host_port = None
        self._mod_name = None
        self._mod_version = None
        self._mod_config = None
        self._gametype = None
        self._mapname = None
        self._allies_cycle = None
        self._axis_cycle = None
        self._winner = None
        self._rounds = []
        self._helper = Helper()


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
        self._start_time = start_time


    @property
    def end_time( self ) -> int:
        return self._end_time


    @end_time.setter
    def end_time( self, end_time: int ):
        self._end_time = end_time


    @property
    def host_address( self ) -> list:
        return self._host_address


    @host_address.setter
    def host_address( self, host_address: list ):
        self._host_address = host_address


    @property
    def host_port( self ) -> int:
        return self._host_port


    @host_port.setter
    def host_port( self, host_port: int ):
        self._host_port = host_port


    @property
    def mod_name( self ) -> str:
        return self._mod_name


    @mod_name.setter
    def mod_name( self, mod_name ):
        self._mod_name = mod_name


    @property
    def mod_version( self ) -> str:
        return self._mod_version


    @mod_version.setter
    def mod_version( self, mod_version: str ):
        self._mod_version = mod_version


    @property
    def mod_config( self ) -> str:
        return self._mod_version


    @mod_config.setter
    def mod_config( self, mod_config: str ):
        self._mod_config = mod_config


    @property
    def gametype( self ) -> int:
        return self._gametype


    @gametype.setter
    def gametype( self, gametype: int ):
        self._gametype = gametype


    @property
    def mapname( self ) -> str:
        return self._mapname


    @mapname.setter
    def mapname( self, mapname: str ):
        self._mapname = mapname


    @property
    def allies_cycle( self ) -> int:
        return self._allies_cycle


    @allies_cycle.setter
    def allies_cycle( self, allies_cycle: int ):
        self._allies_cycle = allies_cycle


    @property
    def axis_cycle( self ) -> int:
        return self._axis_cycle


    @axis_cycle.setter
    def axis_cycle( self, axis_cycle: int ):
        self._axis_cycle = axis_cycle


    @property
    def winner( self ) -> str:
        return self._winner


    @winner.setter
    def winner( self, winner: str ):
        self._winner = winner


    @property
    def rounds( self ) -> list:
        return self._rounds


    @rounds.setter
    def rounds( self, rounds: list ):
        self._rounds = rounds


    # Derivatives

    @property
    def events( self ):
        """
        x
        """

        return self._helper.get_events( self.rounds )


    @property
    def gametype_str( self ) -> str:
        """
        Returns the proper name of the gametype for this match.
        """

        assert self.gametype
        return info.GAMETYPES.get( self.gametype, info.DEFAULT_GAMETYPE )


    @property
    def host_address_str( self ) -> str:
        """
        Returns the full address of the server this match occured on.
        """

        assert self.host_address and self.host_port
        return ".".join( [f"{str( v )}" for v in self.host_address] ) + f":{str( self.host_port )}"


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

        return list( dict.fromkeys( self._helper.get_players( self.rounds )))


    @property
    def size( self ):
        """
        x
        """

        return len( self._helper.get_players( self.rounds ))


    @property
    def stats( self ):
        """
        x
        """

        stats = self._helper.get_stats( self.rounds )
        stats.combine()
        return stats
    

    @property
    def wstats( self ):
        """
        x
        """

        wstats = self._helper.get_wstats( self.rounds )
        wstats.combine()
        return wstats
