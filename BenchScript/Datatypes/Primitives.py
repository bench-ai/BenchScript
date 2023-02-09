class IntegerException(Exception):
    pass


class DoubleException(Exception):
    pass


class StringException(Exception):
    pass


class BooleanException(Exception):
    pass


class Integer(int):
    def __new__(cls, value, *args, **kwargs):
        return super(cls, cls).__new__(cls, value)

    def __add__(self, other):
        return super(Integer, self).__add__(other)

    def __sub__(self, other):
        return super(Integer, self).__sub__(other)

    def __mul__(self, other):
        return super(Integer, self).__mul__(other)

    def __div__(self, other):
        return super(Integer, self).__div__(other)

    def __str__(self):
        return "{}".format(int(self))

    def __repr__(self):
        return "Integer({})".format(int(self))

    def set(self, other):
        if isinstance(other, Integer):
            return self.__new__(Integer, other)
        else:
            raise IntegerException("Cannot make non integer a integer")


class Double(float):
    def __new__(cls, value, *args, **kwargs):
        return super(cls, cls).__new__(cls, value)

    def __add__(self, other):
        return super(Double, self).__add__(other)

    def __sub__(self, other):
        return super(Double, self).__sub__(other)

    def __mul__(self, other):
        return super(Double, self).__mul__(other)

    def __div__(self, other):
        return super(Double, self).__div__(other)

    def __str__(self):
        return "{}".format(float(self))

    def __repr__(self):
        return "Double({})".format(float(self))

    def set(self, other):
        if isinstance(other, Double):
            return self.__new__(Double, other)
        else:
            raise DoubleException("Cannot make non double a double")


class String(str):

    def set(self, other):
        if isinstance(other, String):
            return self.__new__(String, other)
        else:
            StringException("Cannot make non String a String")


class Boolean:

    def __init__(self,
                 val):

        if not isinstance(val, bool):
            raise BooleanException("instance must be of type Boolean")

        self._val = val

    @property
    def val(self):
        return self._val

    def __bool__(self):
        return self.val

    def __str__(self):
        return str(self.val)

    def set(self, other):
        if isinstance(other, Boolean):
            self._val = other.val
        else:
            BooleanException("Cannot make non Boolean a Boolean")

