from .Datatypes.Arrays import IntegerArray, DoubleArray, BoolArray, StringArray, Array
from .Datatypes.Lists import IntegerList, DoubleList
from .Datatypes.Matrices import IntegerMatrix, DoubleMatrix
from .Datatypes.Primitives import String, Boolean, Double, Integer
import dill


class ConvertException(Exception):
    pass


def convert_datatype(dt: str,
                     value,
                     max_len=None):
    match dt:

        case "Integer":
            return Integer(value)
        case "Double":
            return Double(value)
        case "String":
            return String(value)
        case "Boolean":
            return Boolean(value)
        case "IntegerArray":
            return IntegerArray(max_len,
                                [convert_datatype("Integer", i, max_len=None) for i in value])
        case "DoubleArray":
            return DoubleArray(max_len,
                               [convert_datatype("Double", i, max_len=None) for i in value])
        case "StringArray":
            return StringArray(max_len,
                               [convert_datatype("String", i, max_len=None) for i in value])
        case "BooleanArray":
            return BoolArray(max_len,
                             [convert_datatype("Boolean", i, max_len=None) for i in value])
        case "IntegerList":
            return IntegerList([convert_datatype("Integer", i, max_len=None) for i in value])
        case "DoubleList":
            return DoubleList([convert_datatype("Double", i, max_len=None) for i in value])
        case "IntegerMatrix":
            return IntegerMatrix([convert_datatype("IntegerList", i, max_len=None) for i in value])
        case "DoubleMatrix":
            return DoubleMatrix([convert_datatype("DoubleList", i, max_len=None) for i in value])
        case _:
            raise ConvertException("invalid datatype was sent")


def convert_to_pickle(code, f_name: str):
    namespace = {}
    exec(code, namespace)
    with open(f_name, "wb") as f:
        dill.dump(namespace["run"], f)


def get_shape(arg_dict, pickle_file):
    with open(pickle_file, "rb") as file:
        func = dill.load(file)
        return func(arg_dict)
