"""
x
"""

# Global Imports

from time import time


# Local Imports

import lib.constants as info


class Match( object ):
    """
    x
    """

    def __init__( self, match_id: int ):
        """
        Parameters
        ----------
        match_id : int
            The unique identifier for this match.
        """

        assert match_id > 0
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


    def __str__( self ):
        string = f"match_id: {self.match_id}\n"
        string += f"start_time: {self.start_time}\n"
        string += f"end_time: {self.end_time}\n"
        string += f"host_address: {self.host_address}\n"
        string += f"host_port: {self.host_port}\n"
        string += f"host_address_str: {self.host_address_str}\n"
        string += f"mod_name: {self.mod_name}\n"
        string += f"mod_version: {self.mod_version}\n"
        string += f"gametype: {self.gametype}\n"
        string += f"gametype_str: {self.gametype_str}\n"
        string += f"mapname: {self.mapname}\n"
        string += f"allies_cycle: {self.allies_cycle}\n"
        string += f"axis_cycle: {self.axis_cycle}\n"
        string += f"winner: {self.winner}\n"
        string += f"rounds:\n"
        for element in self.rounds:
            string += f"{info.LINE_BREAK}\n"
            string += f"{element}"
        string += f"players:\n"
        string += f"size:\n"
        return string


    def __lt__( self, other: object ):
        return self.match_id < other.match_id


    def __le__( self, other: object ):
        return self.match_id <= other.match_id


    def __eq__( self, other: object ):
        return self.match_id == other.match_id


    def __ne__( self, other: object ):
        return self.match_id != other.match_id


    def __ge__( self, other: object ):
        return self.match_id >= other.match_id


    def __gt__( self, other: object ):
        return self.match_id > other.match_id


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
    def mod_name( self ) -> str:
        return self._mod_name


    @mod_name.setter
    def mod_name( self, mod_name ):
        assert 0 < len( mod_name ) < 32
        self._mod_name = mod_name


    @property
    def mod_version( self ) -> str:
        return self._mod_version


    @mod_version.setter
    def mod_version( self, mod_version: str ):
        assert 0 < len( mod_version ) < 32
        self._mod_version = mod_version


    @property
    def mod_config( self ) -> str:
        return self._mod_version


    @mod_config.setter
    def mod_config( self, mod_config: str ):
        assert len( mod_config ) == 32
        self._mod_config = mod_config


    @property
    def gametype( self ) -> int:
        return self._gametype


    @gametype.setter
    def gametype( self, gametype: int ):
        assert gametype in info.GAMETYPES
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
        assert 0 < allies_cycle < 60
        self._allies_cycle = allies_cycle


    @property
    def axis_cycle( self ) -> int:
        return self._axis_cycle


    @axis_cycle.setter
    def axis_cycle( self, axis_cycle: int ):
        assert 0 < axis_cycle < 60
        self._axis_cycle = axis_cycle


    @property
    def winner( self ) -> str:
        return self._winner


    @winner.setter
    def winner( self, winner: str ):
        assert not winner or winner in info.TEAMS.values()
        self._winner = winner


    @property
    def rounds( self ) -> list:
        return self._rounds


    @rounds.setter
    def rounds( self, rounds: list ):
        self._rounds = rounds


    @property
    def length( self ):
        """
        Returns the total active time of this match.
        """

        length = 0
        if self.rounds:
            for element in self.rounds:
                length += element.length
        return length


    @property
    def players( self ):
        """
        Returns the list of players in this match.
        """

        players = set()
        if self.rounds:
            for element in self.rounds:
                players.update( element.players )
        return len( players )


    @property
    def size( self ):
        """
        Returns the number of players in this match.
        """

        return len( self.players )


    # Derivatives

    @property
    def gametype_str( self ) -> str:
        """
        Returns the proper name of the gametype for this match.
        """

        assert self.gametype
        return info.GAMETYPES.get( self.gametype, "unknown" )


    @property
    def host_address_str( self ) -> str:
        """
        Returns the full address of the server this match occured on.
        """

        assert self.host_address and self.host_port
        return ".".join( [f"{str( v )}" for v in self.host_address] ) + f":{str( self.host_port )}"


    # Input Validation

    def _validate_round_id( self, round_id: int ):
        """
        x

        Parameters
        ----------
        round_id : int
            x
        """

        assert round_id in info.ROUNDS
