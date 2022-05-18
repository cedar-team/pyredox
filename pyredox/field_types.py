# -*- coding: utf-8 -*-


class Number(float):
    """A float with extra awesome actions!

    Without this type defined and available for Redox fields, there are some
    edge cases where testing equality of values can yield some unexpected
    failures, such as 15.0 != "15". Overloading the parent methods for
    ``str`` and ``repr`` corrects this problem.
    """

    def __repr__(self):
        return int(self).__repr__() if self == int(self) else super().__repr__()

    def __str__(self):
        return int(self).__str__() if self == int(self) else super().__str__()
