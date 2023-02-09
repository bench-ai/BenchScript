from .Primitives import Integer, Double, String, Boolean


class ArrayException(Exception):
    pass


class Array(list):

    def __init__(self,
                 max_length: Integer,
                 starter_list=None):

        self._max_len = max_length

        super().__init__()
        ls = [] if not starter_list else starter_list

        if ls:
            if len(ls) > max_length:
                raise ArrayException("Initial array size is too small for provided array")
            self.extend(ls)

    @property
    def max_len(self):
        return self._max_len

    @max_len.setter
    def max_len(self, i: Integer):
        self._max_len = self.max_len.set(i)

    def append(self,
               val):
        if (1 + len(self)) > self.max_len:
            raise ArrayException("Array does not have enough space to store these values")

        super().append(val)

    def extend(self,
               new_list: list):

        for i in new_list:
            self.append(i)

    def insert(self,
               idx: int,
               item):

        if idx >= self.max_len:
            raise ArrayException("index is not available")
        else:
            super().insert(idx, item)

    def set(self,
            other):

        if len(other) > self.max_len:
            raise ArrayException("list is too long to set")

        return other


class IntegerArray(Array):

    def __init__(self,
                 max_length: Integer,
                 new_arr: list[Integer]):

        super().__init__(max_length, new_arr)

    def append(self,
               val: Integer):

        if not isinstance(val, Integer):
            raise ArrayException("Array can only contain type Integer not type {}".format(type(i)))

        super().append(val)

    def insert(self,
               idx: int,
               item: Integer):

        if not isinstance(item, Integer):
            raise ArrayException("Array can only contain type Integer not type {}".format(type(item)))

        super().insert(idx, item)

    def set(self,
            other):

        for i in other:
            if not isinstance(i, Integer):
                raise ArrayException("Values must all be of type Integer")

        return super().set(other)

    def __setitem__(self, key, value):
        if not isinstance(value, Integer):
            raise ArrayException("Array can only contain type Integer not type {}".format(type(value)))
        super().__setitem__(key, value)


class DoubleArray(Array):

    def __init__(self,
                 max_length: Integer,
                 new_arr: list[Double]):

        super().__init__(max_length, new_arr)

    def append(self,
               val: Double):

        if not isinstance(val, (Integer, Double)):
            raise ArrayException("Array can only contain type Double not type {}".format(type(i)))

        super().append(val)

    def insert(self,
               idx: int,
               item: Double):

        if not isinstance(item, (Integer, Double)):
            raise ArrayException("Array can only contain type Double not type {}".format(type(item)))

        super().insert(idx, Double(item))

    def set(self,
            other: Array):

        other_list = []
        for i in other:
            if not isinstance(i, (Integer, Double)):
                raise ArrayException("Values must all be of type Double")

            other_list.append(Double(i))

        return super().set(other_list)

    def __setitem__(self, key, value):
        if not isinstance(value, Double):
            raise ArrayException("Array can only contain type Double not type {}".format(type(value)))
        super().__setitem__(key, value)


class StringArray(Array):

    def __init__(self,
                 max_length: Integer,
                 new_arr: list[String]):

        super().__init__(max_length, new_arr)

    def append(self,
               val: String):

        if not isinstance(val, String):
            raise ArrayException("Array can only contain type str not type {}".format(type(i)))

        super().append(val)

    def insert(self,
               idx: Integer,
               item: String):

        if not isinstance(item, String):
            raise ArrayException("Array can only contain type str not type {}".format(type(item)))

        super().insert(idx, item)

    def set(self,
            other):

        for i in other:
            if not isinstance(i, String):
                raise ArrayException("Values must all be of type str")

        return super().set(other)

    def __setitem__(self, key, value):
        if not isinstance(value, String):
            raise ArrayException("Array can only contain type String not type {}".format(type(value)))
        super().__setitem__(key, value)


class BoolArray(Array):

    def __init__(self,
                 max_length: Integer,
                 new_arr: list[Boolean]):

        super().__init__(max_length,
                         new_arr)

    def append(self,
               val: Boolean):

        if not isinstance(val, Boolean):
            raise ArrayException("Array can only contain type bool not type {}".format(type(i)))

        super().append(val)

    def insert(self,
               idx: Integer,
               item: Boolean):

        if not isinstance(item, Boolean):
            raise ArrayException("Array can only contain type bool not type {}".format(type(item)))

        super().insert(idx, item)

    def set(self,
            other):

        for i in other:
            if not isinstance(i, Boolean):
                raise ArrayException("Values must all be of type str")

        return super().set(other)

    def __setitem__(self, key, value):
        if not isinstance(value, Boolean):
            raise ArrayException("Array can only contain type Boolean not type {}".format(type(value)))
        super().__setitem__(key, value)
