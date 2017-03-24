"""This module evaluates a postfix arithmetic expression
given an iterator that refers to a sequence of tokens.
This solution is intended for the benefit of the students
taking CMPSC 122 at the Pennsylvania State University
during the Spring Semester of 2017, and is not intended
for any other audience, or to distributed outside of the course.

Roger Christman, Pennsylvania State University
"""
class VarTree:
    """A simple binary tree to associate variables with values"""
    class Node:
        """A simple tree node, with no parent link"""
        __slots__ = "_name", "_value","_left","_right"
        def __init__(self,l,var,val,r):
            self._name = var
            self._value = val
            self._left = l
            self._right = r
    def __init__(self):
        self._root = None
        self._size = 0
    def _search( self, here, var ):
        """search for a variable, returning Node (None if not found)"""
        if here is None:
            return None
        elif here._name == var:
            return here
        elif here._name > var:
            return self._search( here._left, var )
        else:
            return self._search( here._right, var )
    def _insert( self, here, var, value ):
        """returns new tree with new variable added or updated"""
        if here is None:
            self._size += 1
            return self.Node( None, var, value, None )
        elif here._name == var:
            return self.Node( here._left, var, value, here._right )
        elif here._name > var:
            return self.Node( self._insert( here._left, var, value ),
                              here._name, here._value, here._right )
        else:
            return self.Node( here._left, here._name, here._value,
                              self._insert( here._right, var, value ))
    def assign( self, var, val ):
        """Assign value to named variable, by creating a new tree
        root is assigned to refer to the new tree
        """
        self._root = self._insert( self._root, var, val )
    def lookup( self, var ):
        """Search for a variable and return its value
        Assigns value of 0 if not present
        """
        node = self._search( self._root, var )
        if node is None:
            self.assign( var, 0 )
            return 0
        else:
            return node._value
    def is_empty( self ):
        return self._root is None
    def __len__( self ):
        return self._size
    def _rec_iter(self,here):
        if here is not None:
            yield from self._rec_iter(here._left)
            yield here._name, here._value
            yield from self._rec_iter(here._right)
    def __iter__( self ):
        if self._root is not None:
            yield from self._rec_iter(self._root)
    def __str__( self ):
        return ', '.join( name + '=' + str(val) for name,val in iter(self))

if __name__ == '__main__':
    V = VarTree()
    print("Empty?",V.is_empty())
    V.assign( "PI", 3.14 )
    V.assign( "e", 2.718 )
    V.assign( "x", 4 )
    V.assign( "y", 5 )
    print("x = ",V.lookup("x"))
    print("Z = ",V.lookup("Z"))
    print( list(V) )
    print( V )
    print("Empty?",V.is_empty(),"contains",len(V),"entries")
            
