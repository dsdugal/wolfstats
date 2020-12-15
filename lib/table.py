"""
x
"""

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

        assert len( headers ) > 1 # len of default_headers?
        assert len( body ) > 1 # min number of players
        self._headers = headers
        self._body = body
        self._sums = [ 0 for v in self.headers ]
        self._summarize( 0, len( self.headers ))


    def __str__( self ):
        string = ""
        string += ",".join( self.headers ) + "\n"
        for row in self.body:
            string += ",".join( str( value ) for value in row ) + "\n"
        string += ",".join( str( value ) for value in self.sums ) 
        return string


    # Properties

    @property
    def body( self ) -> list:
        return self._body


    @property
    def headers( self ) -> list:
        return self._headers


    @property
    def sums( self ) -> list:
        return self._sums


    @sums.setter
    def sums( self, sums ) -> list:
        self.sums = sums


    # Derivatives

    @property
    def columns( self ) -> int:
        """
        Returns the number of columns (categories) in this table.
        """

        return len( self.body[0] )


    @property
    def rows( self ) -> int:
        """
        Returns the number of rows (players) in this table.
        """

        return len( self.body )


    # Private Methods

    def _summarize( self, start, limit ):
        """
        Populates the sum of each column in a table within the given range.

        Parameters
        ----------
        start : int
            The first index in the range.
        limit : int
            The last index in the range (exclusive).
        """

        for i in range( start, limit ):
            if self.headers[i] not in info.DEFAULT_HEADERS:
                self.sums[i] = self.column_sum( i )
            else:
                self.sums[i] = None


    # Public Methods

    def column_data( self, column: int, select: int = None, value = None ) -> list:
        """
        Returns a list that contains the values in a column of a table.

        Parameters
        ----------
        column : int
            The column to look for data in.
        select : int
            The column to filter results by.
        value : object
            The value to filter results by.
        """

        if select:
            return [ row[column] for row in self.body if row[select] == value ]
        else:
            return [ row[column] for row in self.body ]


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

        data = self.column_data( column, select, value )
        if all( isinstance( v, ( float, int )) for v in data ):
            return sum( data )
        else:
            return None
