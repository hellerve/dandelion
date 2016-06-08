"""An augmented version of the dict class"""
from dandelion.computed import PY3
from dandelion.classes.iterable import Iterable
from dandelion.classes.repr import Repr
from dandelion.classes.collection import Collection

class Dict(Repr, dict, Iterable, Collection):
    """An augmented version of the dict class"""
    def reset(self, other):
        """
        Resets a dict to another dicts content

        Complexity: O(n)
        params:
            other: the dict this dict should be resetted to
        returns: self
        """
        self.clear()
        self.update(other)
        return self

    def reverse(self):
        """
        Exchanges keys and values; if there are duplicate values, the last value that's been written wins.

        Complexity: O(2*n)
        returns: self
        """
        tmp = dict()
        for key, val in self.items():
            tmp[val] = key
        self.reset(tmp)
        del tmp
        return self

    def remove_empty(self, fun=None, filter_keys=False):
        """
        Removes empty pairs from the dict.

        Complexity: O(2*n)
        params:
            fun: a function that takes an element and returns whether it should be kept (defaults to bool())
            filter_keys: a flag that indicates that filtering should be done by keys, not by values
        returns: self
        """
        if not fun:
            fun = bool
        tmp = dict()
        for key, val in self.items():
            if filter_keys:
                if fun(key): tmp[key] = val
            else:
                if fun(val): tmp[key] = val
        self.reset(tmp)
        del tmp
        return self

    def update(self, *args, **kwargs):
        """
        Update dictionary. Same as in dict(), but returns self.

        returns: self
        """
        super(Dict, self).update(*args, **kwargs)
        return self

    def reduce(self, fun, acc=None):
        """
        Reduce the dict to a value (using function fun).

        Complexity: O(n)
        params:
            fun: a function that takes the accumulator and current key and value and returns the new accumulator
            acc: the initial accumulator (defaults to tuple of first key and value taken from the iterator)
        returns: self
        """
        iterator = self.items().__iter__()
        if acc is None:
            acc = iterator.__next__() if PY3 else iterator.next()
        for key, val in iterator:
            acc = fun(acc, key, val)
        return acc

    def clear(self):
        """
        Augmented clear function that returns self.

        returns: self
        """
        super(Dict, self).clear()
        return self

    def setdefault(self, *args, **kwargs):
        """
        Augmented setdefault function that returns self.

        returns: self
        """
        super(Dict, self).setdefault(*args, **kwargs)
        return self
