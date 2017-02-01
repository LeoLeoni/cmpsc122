class Peekable():
    """An iterator with the ability to examine a value without advancement"""

    def __init__(self, iterator):
        """Take an existing iterator and add peek functionality
        iterator    -- the previous 'ordinary iterator
    """
        self._iterator = iterator
        self._peeked = None

    #   the following two methods meet the protocol for iterators

    def __iter__(self):
        return self

    def __next__(self):
        """return the next element of the data (as would be expected)
    no advancement occurs if that element has already been peeked at
    """
        if self._peeked is None:
            self._peeked = next(self._iterator)
        ans = self._peeked
        self._peeked = None     # we don't yet see what comes next
        return ans

    def peek(self):
        """peek at the next element of the data
    only advancing if that next item has not yet been peeked at
    """
        if self._peeked is None:
            try:
                self._peeked = next(self._iterator)
            except StopIteration:
                self._peeked = None
        return self._peeked


# this function is defined just to allow similarity to next()
def peek(x):
    return x.peek()