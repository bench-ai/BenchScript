from .Primitives import Integer, Double


class ListException(Exception):
    pass


class IntegerList(list):

    def __init__(self,
                 new_arr: list[Integer]):

        super().__init__(new_arr)

    def append(self,
               val: Integer):

        if not isinstance(val, Integer):
            raise ListException("List can only contain type Integer not type {}".format(type(val)))

        super().append(val)

    def insert(self,
               idx: int,
               item: Integer):

        if not isinstance(item, Integer):
            raise ListException("List can only contain type Integer not type {}".format(type(item)))

        super().insert(idx, item)

    def __setitem__(self, key, value):
        if not isinstance(value, Integer):
            raise ListException("List can only contain type Integer not type {}".format(type(value)))
        super().__setitem__(key, value)

    def set(self,
            other):

        for i in other:
            if not isinstance(i, Integer):
                raise ListException("Values must all be of type Integer")

        return other


class DoubleList(list):

    def __init__(self,
                 new_arr: list[Double]):

        super().__init__(new_arr)

    def append(self,
               val: Double):

        if not isinstance(val, Double):
            raise ListException("List can only contain type Double not type {}".format(type(val)))

        super().append(val)

    def insert(self,
               idx: int,
               item: Double):

        if not isinstance(item, Integer):
            raise ListException("List can only contain type Double not type {}".format(type(item)))

        super().insert(idx, item)

    def __setitem__(self, key, value):
        if not isinstance(value, Double):
            raise ListException("List can only contain type Double not type {}".format(type(value)))
        super().__setitem__(key, value)

    def set(self,
            other):

        for i in other:
            if not isinstance(i, Double):
                raise ListException("Values must all be of type Double")

        return other
