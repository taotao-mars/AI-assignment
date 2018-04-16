


class cell(object):
    """
    A cell in a grid. Cells have the
    following properties:

    Attributes:
        isBlocked: Boolean value indicating whether a cell is blocked or not
    """

    def __init__(self,r,c):
        """
        Return a cell object with initial values.
        """
        self.row = r
        self.column = c
        self.blocked = False
        
    def setBlocked(self,value):
        """
        Sets the cell blocked value
        """
        self.blocked = value
        
    def isBlocked(self):
        """
        Returns the value of blocked
        """
        return self.blocked