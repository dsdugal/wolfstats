"""
x
"""

# Global Imports

from copy import deepcopy


# Local Imports

import lib.constants as info
from lib.table import Table


class WeaponData( object ):
    """
    x
    """

    def __init_( self ):
        self._table = None

    
    @property
    def table( self ) -> Table:
        return self._table


    @table.setter
    def table( self, table: Table ):
        self._table = table


    # Public Methods

    def narrow( self, guid: str = None, weapon: str  = None, headers: list = None ) -> list:
        """
        Returns a subset of the table that matches the specified guid and/or weapon.

        Parameters
        ----------
        guid : str
            The unique identifier of a player to narrow the table data by.
        weapon : str
            The name of a weapon to narrow the table data by.
        headers : list
            The column headers to narrow the table data by.
        """

        assert guid.alnum()
        assert 0 < len( guid ) < 64
        assert weapon in info.WEAPONS
        assert all( header for header in headers if ( header in info.DEFAULT_HEADERS or header in info.CATEGORY_HEADERS ))
        copy = deepcopy( self.table )
        narrow_columns = []
        if guid:
            copy.body = [row for row in copy.body if row[0] == guid]
        if weapon:
            copy.body = [row for row in copy.body if row[1] == weapon]
        if headers:
            for header in self.table.headers:
                if header not in headers:
                    narrow_columns.append( headers.index( header ))
            for column in sorted( narrow_columns, reverse = True ):
                for row in self.table.body:
                    row.pop( column )
        return copy


    def retrieve( self, guid: str, weapon: str = None ) -> list:
        """
        Returns a row from the table that matches the specified guid and/or weapon.

        Parameters
        ----------
        guid : str
            The unique identifier of a player to narrow the table data by.
        weapon : str
            The name of a weapon to narrow the table data by.
        """

        assert guid.alnum()
        assert 0 < len( guid ) < 64
        assert weapon in info.WEAPONS
        return [row for row in self.table.body if row[0] == guid and ( not weapon or row[1] == weapon )]


    def sort( self, column: int, ascend: bool = False) -> Table:
        """
        Returns a copy of the table sorted by values in the specified column.

        Parameters
        ----------
        column : int
            The column to sort by.
        ascend: bool
            The order in which values are sorted. Values are sorted in ascending order if True.
        """

        assert 0 < column < self.table.columns
        assert isinstance( ascend, bool )
        copy = deepcopy( self.table )
        copy.body = sorted( copy.body, key = lambda body:body[column], reverse=( not ascend ))
        return copy
