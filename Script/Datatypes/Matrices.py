from .Lists import IntegerList, DoubleList
from .Primitives import Integer


class MatrixException(Exception):
    pass


class Matrix(list):

    def __init__(self,
                 new_arr: list[list]):

        super().__init__()
        for i in new_arr:
            self.append(i)

    def append(self,
               val: list):

        t_list = tuple(val)

        if len(self) == 0:
            super().append(t_list)
        else:
            if len(self[0]) != len(t_list):
                raise MatrixException("All rows of the matrix must be the same length")
            else:
                super().append(t_list)

    def insert(self,
               idx: Integer,
               item: list):

        t_list = tuple(item)

        if len(self) == 0:
            super().insert(idx, t_list)
        else:
            if len(self[0]) != len(t_list):
                raise MatrixException("All rows of the matrix must be the same length")
            else:
                super().insert(idx, t_list)

    def __setitem__(self, key, value):
        t_list = tuple(value)
        if len(self[0]) != len(t_list):
            raise MatrixException("new row of the matrix must be the same length")
        else:
            super().__setitem__(key, value)

    def set(self,
            other):

        return other


class IntegerMatrix(Matrix):

    def __init__(self,
                 new_arr: list[IntegerList]):

        for i in new_arr:
            if not isinstance(i, IntegerList):
                raise MatrixException("Only a List of IntegerLists are acceptable")

        super().__init__(new_arr)

    def append(self,
               val: IntegerList):

        if not isinstance(val, IntegerList):
            raise MatrixException("Only a List of IntegerLists are acceptable")

        super().append(val)

    def insert(self,
               idx: Integer,
               item: IntegerList):

        if not isinstance(item, IntegerList):
            raise MatrixException("Only a List of IntegerLists are acceptable")

        super().insert(idx, item)

    def __setitem__(self, key, value):
        if not isinstance(value, IntegerList):
            raise MatrixException("Only IntegerLists are allowed as rows")

        super().__setitem__(key, value)

    def set(self,
            other: Matrix):

        if isinstance(other, IntegerMatrix):
            return super().set(other)
        else:
            raise MatrixException("Cannot set a integer matrix to a non integer matrix")


class DoubleMatrix(Matrix):

    def __init__(self,
                 new_arr: list[DoubleList]):

        for i in new_arr:
            if not isinstance(i, DoubleList):
                raise MatrixException("Only a List of DoubleLists are acceptable")

        super().__init__(new_arr)

    def append(self,
               val: DoubleList):

        if not isinstance(val, DoubleList):
            raise MatrixException("Only a List of DoubleLists are acceptable")

        super().append(val)

    def insert(self,
               idx: Integer,
               item: DoubleList):

        if not isinstance(item, DoubleList):
            raise MatrixException("Only a List of DoubleLists are acceptable")

        super().insert(idx, item)

    def __setitem__(self, key, value):
        if not isinstance(value, DoubleList):
            raise MatrixException("Only DoubleLists are allowed as rows")

        super().__setitem__(key, value)

    def set(self,
            other: Matrix):

        if isinstance(other, DoubleMatrix):
            return super().set(other)
        else:
            raise MatrixException("Cannot set a double matrix to a non double matrix")
