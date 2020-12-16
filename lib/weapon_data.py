"""

    guid, weapon, [ kills, deaths, shots, hits, accuracy, headshots, headshot accuracy, damage_given, damage_taken, team_damage_given, team_damage_taken ]

"""

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

    def narrow( self, guid: str = None, weapon: str  = None) -> list:
        """
        Returns a subset of the table that matches the specified guid and/or weapon.

        Parameters
        ----------
        guid : str
            x
        weapon : str
            x
        """

        pass


    def retrieve( self, guid: str, context: dict) -> list:
        """
        Returns a value from the table that matches the specified context.

        Parameters
        ----------
        guid : str
            x
        context : dict
            x
        """

        pass


    def sort( self, column: int, ascend: bool = True) -> Table:
        """
        Returns a copy of the table sorted by values in the specified column.

        Parameters
        ----------
        column : int
            The column to sort by.
        ascend: bool
            The order in which values are sorted. Values are sorted in ascending order if True.
        """

        pass

"""
    columns
    rows
    column_data
    column_sums
"""