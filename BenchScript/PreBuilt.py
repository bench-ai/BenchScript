import copy
from BenchScript.Datatypes.Primitives import Integer, Double, Boolean, String
from BenchScript.Datatypes.Arrays import StringArray, Array
import sympy


def equation(eqt_str: String,
             symbol_list: StringArray,
             *args) -> Double:
    """
    :argument returns the value of a equation
    :param eqt_str: the equation to run
    :param symbol_list: the list of symbols in the list
    :param args: the values of each symbol
    :return: the value of the equation
    """

    sympy_list = [sympy.symbols(s) for s in symbol_list]
    zip_list = list(zip(sympy_list, args))
    eqt = sympy.sympify(eqt_str)
    v = eqt.subs(zip_list)
    return Double(v)


def equals(value_one,
           value_two, ) -> Boolean:
    """
    :argument whether two values are equal
    :param value_one: The first comparative argument
    :param value_two: The first comparative argument
    :return:
    """
    return Boolean(Double(value_one) == Double(value_two))


def opp(value_one: Boolean) -> Boolean:
    """
    :argument make boolean opposite
    :param value_one: The first comparative argument
    :param value_two: The first comparative argument
    :return:
    """
    return Boolean(not value_one)


def append(a: Array, val):
    """
    :argument: appends a value to the array
    :param a: The array we are appending too
    :param val: The value being appended
    """
    a.append(val)


def get_index(a: list,
              *args):
    ac = copy.deepcopy(a)

    for ar in args:
        ac = ac[ar]

    return ac


def set_index(a: list,
              index: Integer,
              value):

    a[index] = value


def insert(a: list, val, ind: Integer):
    """
    :argument: inserts a value to the array
    :param a: The array we are inserting too
    :param val: The value being inserted
    :param ind: The index where the insertion occors
    """
    a.insert(ind, val)


def floor(i: Double) -> Integer:
    return Integer(i)


def pop(i: list, idx=-1):
    return i.pop(idx)


def format_string(string: String, *args):
    return string.format(*args)
