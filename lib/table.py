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

        self._headers = headers
        self._body = body
        self._sums = [ info.PLACEHOLDER for v in self._headers ]
        self._summarize( 0, self.columns - 1 )


    # Properties

    @property
    def headers( self ) -> list:
        return self._headers


    @property
    def body( self ) -> list:
        return self._body


    @body.setter
    def body( self, body: list ):
        self.body = body


    @property
    def sums( self ) -> list:
        return self._sums


    @sums.setter
    def sums( self, sums: list ):
        self.sums = sums


    # Derivatives

    @property
    def columns( self ) -> int:
        """
        Returns the number of columns in the table.
        """

        return len( self.headers )


    @property
    def rows( self ) -> int:
        """
        Returns the number of rows in the table.
        """

        return len( self.body )


    # Private Methods

    def _summarize( self, start, end ):
        """
        Calculates the sum of the values in each column of the table body and stores it in sums.

        Parameters
        ----------
        start : int
            The first column in the table to calculate a sum for.
        end : int
            The last column in the table to calculate a sum for.
        """

        for i in range( start, end + 1 ):
            if self.headers[i] not in info.DEFAULT_HEADERS:
                self.sums[i] = self.column_sum( i )
            else:
                self.sums[i] = info.PLACEHOLDER


    # Public Methods

    def column_avg( self, column: int, select: int = None, value = None ) -> int:
        """
        Returns the average of the values in a column of the table body.

        Parameters
        ----------
        column : int
            The column to look for data in.
        select : int
            The column to filter results by.
        value : object
            The value to filter results by.
        """

        data = self.column_data( column, select, value )
        if all( isinstance( v, ( float, int )) for v in data ):
            return sum( data ) / len( data )
        else:
            return info.PLACEHOLDER


    def column_data( self, index: int, select: int = None, value = None ) -> list:
        """
        Returns the values in a column of the table body.

        Parameters
        ----------
        index : int
            The index of the column to look for data in.
        select : int
            The index of the column to filter results by.
        value : object
            The value to filter results by.
        """

        return [ row[index] for row in self.body if ( select == None or row[select] == value )]


    def column_max( self, index: int, select: int = None, value = None ) -> int:
        """
        Returns the maximum value in a column of the table body.

        Parameters
        ----------
        index : int
            The index of the column to look for data in.
        select : int
            The index of the column to filter results by.
        value : object
            The value to filter results by.
        """

        data = self.column_data( index, select, value )
        if all( isinstance( v, ( float, int )) for v in data ):
            return max( data )
        else:
            return info.PLACEHOLDER


    def column_min( self, index: int, select: int = None, value = None ) -> int:
        """
        Returns the maximum value in a column of the table body.

        Parameters
        ----------
        index : int
            The index of the column to look for data in.
        select : int
            The index of the column to filter results by.
        value : object
            The value to filter results by.
        """

        data = self.column_data( index, select, value )
        if all( isinstance( v, ( float, int )) for v in data ):
            return min( data )
        else:
            return info.PLACEHOLDER


    def column_sum( self, index: int, select: int = None, value = None ) -> int:
        """
        Returns the sum of the values in a column of table body.

        Parameters
        ----------
        index : int
            The index of the column to look for data in.
        select : int
            The index of the column to filter results by.
        value : object
            The value to filter results by.
        """

        data = self.column_data( index, select, value )
        if all( isinstance( v, ( float, int )) for v in data ):
            return sum( data )
        else:
            return info.PLACEHOLDER


    def combine( self ):
        """
        Combines all rows in the body of a table that have the same primary key. 
        """

        self.body.sort()
        k = len( info.DEFAULT_HEADERS )
        previous = self.body[-1]
        for i in range( len( self.body ) - 2, -1, -1 ):
            current = self.body[i]
            if current[0] == previous[0]:
                self.body[i][k:] = [i + j for i, j in zip( previous[k:], current[k:] )]
                self.body.pop( i + 1 )
            previous = current


    def row_data( self, value: object ) -> list:
        """
        Returns the data for a row in the table where value matches the key column.

        Parameters
        ----------
        value : object
            The value to search for in the key column.
        """

        return [row for row in self.body if row[0] == value]


    def sort( self, index: int, ascend: bool = False) -> object:
        """
        Sorts the body of the table by values in the specified column.

        Parameters
        ----------
        index : int
            The index of the column to sort by.
        ascend: bool
            The order in which values are sorted. Values are sorted in ascending order if True.
        """

        self.body.sort( key = lambda row: row[index], reverse = ( not ascend ))


    def subset( self, index: int = None, value: object = None, categories: list = None ): # -> Table
        """
        Returns a subset of the table that matches the specified keys and/or headers.

        Parameters
        ----------
        index: : int
            The index of the column to be used to search for the key.
        value : object
            The element in an indexed column to be matched when returning the subset of a table.
        categories : list
            The list of category headers that specify which data to keep in the subset of a table.
        """

        copy = deepcopy( self )
        cull = []
        if index and value:
            copy.body = [row for row in copy.body if row[index] == value]
        if categories:
            for header in self.headers:
                if header not in categories:
                    cull.append( self.headers.index( header ))
            for column in sorted( cull, reverse = True ):
                copy.headers.pop( column )
                for row in copy.body:
                    row.pop( column )
                copy.sums.pop( column )
        return copy


    def subtract( self, other ):
        """
        Subtracts the data for another round from the table for the current data.

        Parameters
        ----------
        other : Table
            The data for the other round.
        """

        for i in range( self.rows ):
            for j in range( self.columns ):
                value = other.body[i][j]
                if isinstance( value, ( float, int )):
                    self.body[i][j] -= value
