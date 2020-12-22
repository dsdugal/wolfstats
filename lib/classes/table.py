"""
x
"""

# Global Imports

from copy import deepcopy


# Local Imports

import lib.constants as info


class Table( object ):
    """
    x
    """

    def __init__( self, headers: list, body: list ):
        """
        Parameters
        ----------
        headers : list
            A list that contains the header names for each statistical category.
        body : list
            A two dimensional matrix that holds statistical counts for each player in each category.
        """

        assert len( headers ) >= len( info.DEFAULT_HEADERS )
        #assert len( body ) > 1
        self._headers = headers
        self._body = body
        self._sums = [ 0 for v in self.headers ]
        self._summarize( 0, len( self.headers ))


    def __str__( self ):
        string = ",".join( self.headers ) + "\n"
        for row in self.body:
            string += ",".join( str( value ) for value in row ) + "\n"
        string += ",".join( str( value ) for value in self.sums ) 
        return string


    # Properties

    @property
    def headers( self ) -> list:
        return self._headers


    @property
    def body( self ) -> list:
        return self._body


    @body.setter
    def body( self, body ):
        self.body = body


    @property
    def sums( self ) -> list:
        return self._sums


    @sums.setter
    def sums( self, sums ):
        self.sums = sums


    # Derivatives

    @property
    def columns( self ) -> int:
        """
        Returns the number of columns (categories) in this table.
        """

        return len( self.headers )


    @property
    def rows( self ) -> int:
        """
        Returns the number of rows (players) in this table.
        """

        return len( self.body )


    # Private Methods

    def _summarize( self, start, limit ):
        """
        x
        """

        for i in range( start, limit ):
            if self.headers[i] not in info.DEFAULT_HEADERS:
                self.sums[i] = self.column_sum( i )
            else:
                self.sums[i] = info.PLACEHOLDER


    # Input Validation

    def _validate_index( self, index: int = None ):
        """
        x
        """

        if index:
            assert 0 <= index < self.columns

    
    # Public Methods

    def column_data( self, column: int, select: int = None, value = None ) -> list:
        """
        x
        """

        return [ row[column] for row in self.body if ( not select or row[select] == value )]


    def column_avg( self, column: int, select: int = None, value = None ) -> int:
        """
        Returns the average of the values in a column of a table.

        Parameters
        ----------
        column : int
            The column to look for data in.
        select : int
            The column to filter results by.
        value : object
            The value to filter results by.
        """

        self._validate_index( column )
        self._validate_index( select )
        data = self.column_data( column, select, value )
        if all( isinstance( v, ( float, int )) for v in data ):
            return sum( data ) / len( data )
        else:
            return info.PLACEHOLDER


    def column_sum( self, column: int, select: int = None, value = None ) -> int:
        """
        Returns the sum of the values in a column of a table.

        Parameters
        ----------
        column : int
            The column to look for data in.
        select : int
            The column to filter results by.
        value : object
            The value to filter results by.
        """

        self._validate_index( column )
        self._validate_index( select )
        data = self.column_data( column, select, value )
        if all( isinstance( v, ( float, int )) for v in data ):
            return sum( data )
        else:
            return info.PLACEHOLDER


    def row_data( self, column1: int, value1: object, column2: int = None, value2: object = None ) -> list:
        """
        Returns a row from the table that matches the specified guid and/or weapon.

        Parameters
        ----------
        column1 : int
            x
        value1 : object
            x
        column2 : int
            x
        value2 : object
            x
        """

        return [row for row in self.body if row[column1] == value1 and ( not value2 or row[column2] == value2 )]


    def sort( self, column: int, ascend: bool = False) -> object:
        """
        Returns a copy of this table sorted by values in the specified column.

        Parameters
        ----------
        column : int
            The column to sort by.
        ascend: bool
            The order in which values are sorted. Values are sorted in ascending order if True.
        """

        assert 0 < column < self.columns
        assert isinstance( ascend, bool )
        copy = deepcopy( self )
        copy.body = sorted( copy.body, key = lambda body:body[column], reverse = ( not ascend ))
        return copy


    def subset( self, value1: object, value2: object = None, copy_headers: list = None ) -> list:
        """
        Returns a subset of the table that matches the specified keys and/or headers.

        Parameters
        ----------
        key1 : object
            x
        key2 : object
            x
        copy_headers : list
            x
        """

        assert all( header for header in copy_headers if header in info.CATEGORY_HEADERS )
        copy = deepcopy( self )
        cull = []
        if value1:
            copy.body = [row for row in copy.body if row[0] == value1]
        if value2:
            copy.body = [row for row in copy.body if row[1] == value2]
        if copy_headers:
            for header in self.headers:
                if header not in copy_headers:
                    cull.append( copy_headers.index( header ))
            for column in sorted( cull, reverse = True ):
                for row in copy.body:
                    row.pop( column )
        return copy
