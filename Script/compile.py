import re


class CompileException(Exception):
    pass


class ScriptCompiler:
    starters = {
        "Integer": "Integer",
        "Double": "Double",
        "String": "String",
        "Boolean": "Boolean"
    }
    loop_starters = ("FOR",)
    splits = {"IntegerArray(": ")",
              "IntegerList(": ")",
              "DoubleList(": ")",
              "DoubleArray(": ")",
              "StringArray(": ")",
              "BooleanArray(": ")",
              "IntegerMatrix(": ")",
              "DoubleMatrix(": ")",
              "<<": ">>",
              "[": "]"}

    def __init__(self):
        self._string_list = []
        self._vars = []
        self._method = []
        self._method_var = []

    def rep_str(self,
                my_str: str):
        reg_list = []
        space_list = []
        count = 0
        start = False
        cur_str = ""
        for i in my_str:
            if not start and i == '"':
                start = True
                reg_list.append([count, cur_str])
                cur_str = '"'
                count += 1
            elif start and i == '"':
                cur_str += '"'
                space_list.append([count, cur_str])
                start = False
                cur_str = ''
                count += 1
            else:
                cur_str += i

        reg_list.append([count, cur_str])
        reg_list = [(count, string.replace(" ", "")) for count, string in reg_list]
        space_list = [(count, string.strip()) for count, string in space_list]

        space_list.extend(reg_list)

        space_list = sorted(space_list, key=lambda x: x[0])
        space_list = [i for _, i in space_list]

        return ''.join(space_list)

    def get_string_split(self,
                         strg: str):
        strg = self.rep_str(strg)
        str_list = []
        stack_list = []
        cur = ""
        cur_start = None

        for i in strg:
            cur += i
            if i == ",":
                if not cur_start:
                    str_list.append(cur[:-1])
                    cur = ""
                elif cur_start and (not stack_list) and (i == ","):
                    str_list.append(cur[:-1])
                    cur = ""
                    cur_start = None

            if not cur_start and (cur in self.splits):
                cur_start = cur
                stack_list.append(True)
            elif cur_start:
                if cur.endswith(cur_start):
                    stack_list.append(True)
                if cur.endswith(self.splits[cur_start]):
                    stack_list.pop()

        str_list.append(cur)

        if str_list == ['']:
            return []
        else:
            return str_list

    @property
    def string_list(self):
        return self._string_list

    def get_var(self,
                name,
                method,
                m_var=False):

        for i in self._method_var if m_var else self._vars:
            if i["name"] == name and (i["method"] == method or i["method"] == self._method[0]):
                return True
        return False

    def if_else_line(self,
                     line: str,
                     iff=False,
                     eliff=False):

        line = line.strip()
        if iff:
            line = line[len("IF"):]
            var = "if"
        elif eliff:
            line = line[len("ELIF"):]
            var = "elif"
        else:
            return "else:"

        line = line.strip("-->")
        line = line.strip()
        vals = self.get_value(line)

        return "{} {}:".format(var, vals)

    def get_proper_data(self,
                        data: str):
        data = data.strip()

        if '"' in data:
            prefix = "String"
        elif not (re.search('[a-zA-Z]', data)) and ("." in data):
            prefix = "Double"
        elif (data == "True") or (data == "False"):
            prefix = "Boolean"
        elif (not re.search('[a-zA-Z]', data)) and ("." not in data):
            prefix = "Integer"
        else:
            prefix = None

        if "Array" in data:
            return data
        if "List" in data:
            return data
        if "Matrix" in data:
            return data
        elif not self.get_var(data, self._method[-1]) and not self.get_var(data, self._method[-1], m_var=True):
            # setting a preexisting variable to a raw value
            if not prefix:
                raise CompileException("Invalid character {}".format(data))
            return "{}({})".format(prefix, data)
        else:
            # setting a preexisting variable to a different prexisting variable
            return "{}".format(data)

    def get_value(self,
                  line):

        line = line.strip()
        ret = ""
        if line.startswith("<<"):
            method_name = ""
            for i in line[2:]:
                if i == ">":
                    break
                method_name += i
            line = line[len("<<{}>".format(method_name)): (-1 * len("<{}>>".format(method_name)))]
            line = line.strip()
            line_list = self.get_string_split(line)
            ret += "{}(".format(method_name)
            a_list = [self.get_value(i) for i in line_list]
            additional_args = ("{}," * len(line_list))[:-1].format(*a_list)
            ret += additional_args + ")"
            return ret

        if "Matrix" in line:
            for i in self.splits:
                if line.startswith(i):
                    line = line.strip(i)
                    break

            value = line.strip(")")
            prefix = i[:-1]
            prefix = prefix.strip()
            value = value.strip()
            value = value[1:-1]
            value = value.strip()
            line_list = self.get_string_split(value)
            ret += "["
            a_list = [self.get_value(i) for i in line_list]
            additional_args = ("{}," * len(line_list))[:-1].format(*a_list)
            ret += additional_args + "]"
            ret = "{}({})".format(prefix, ret)
            return ret
            # return self.get_proper_data(ret)

        if "List" in line:
            for i in self.splits:
                if line.startswith(i):
                    line = line.strip(i)
                    break
            value = line.strip(")")
            prefix = i[:-1]
            prefix = prefix.strip()
            value = value.strip()
            value = value[1:-1]
            value = value.strip()
            line_list = self.get_string_split(value)
            ret += "["
            a_list = [self.get_value(i) for i in line_list]
            additional_args = ("{}," * len(line_list))[:-1].format(*a_list)
            ret += additional_args + "]"
            ret = "{}({})".format(prefix, ret)
            return ret
            # return self.get_proper_data(ret)

        if "Array" in line:
            for i in self.splits:
                if line.startswith(i):
                    line = line.strip(i)
                    break

            value = line.strip(")")
            prefix = i[:-1]
            prefix = prefix.strip()
            value = value.strip()
            max_len, lst = self.get_string_split(value)
            max_len = self.get_value(max_len.strip())
            lst = lst.strip()
            lst = lst[1:-1]
            lst = lst.strip()
            line_list = self.get_string_split(lst)
            ret += "["
            a_list = [self.get_value(i) for i in line_list]
            additional_args = ("{}," * len(line_list))[:-1].format(*a_list)
            ret += additional_args + "]"
            ret = "{}({}, {})".format(prefix, max_len, ret)
            return ret
            # return self.get_proper_data(ret)
        else:
            return self.get_proper_data(line)

    def var_line(self,
                 line: str,
                 first=False):

        line = line.strip()
        if first:

            prefix, value = line.split(":")
            value = value.strip()

            # declare array type

            name, value = value.split("=")
            sname = name.strip()
            value = self.get_value(value)

            self._vars.append({"name": sname,
                               "method": self._method[-1]})

            return "{} = {}".format(sname, value)
        else:
            name, value = line.split("=")
            value = self.get_value(value)
            sname = name.strip()

            return "{} = {}.set({})".format(sname, sname, value)

    def for_line(self,
                 line: str):
        line = line[len("FOR"):]
        line = line.strip("-->")
        line = line.strip()
        var, it = self.get_string_split(line)
        var = self.get_value(var)
        it = self.get_value(it)

        if not self.get_var(var, method=self._method[-1]):
            raise CompileException("Can't use for loop variable without prior declaration")

        ret_str = "for {} in {}:".format(var, it)

        return ret_str

    def method_line(self,
                    line: str):
        line = line[len("METHOD"):]
        line = line.strip("-->")
        line = line.strip()

        name = ""
        start = False
        for letter in line:
            if letter == ">":
                break
            if start:
                name += letter
            if letter == "<":
                start = True

        name = name[1:]
        self._method.append(name)

        l_name = "<<{}>".format(name)
        line = line.strip(l_name)
        line = line.strip()

        line_list = line.split(",")
        line_list = list(map(lambda s: s.split(":")[-1].strip(), line_list))

        for i in line_list:
            self._method_var.append({"method": self._method[-1],
                                     "name": i})

        arg_list = ("{}, " * len(line_list))[:-2].format(*line_list)

        ret_str = "def {}({}):".format(name, arg_list)

        return ret_str, name

    def return_line(self, line):
        line = line.strip()
        line = line[len("RETURN"):]
        l_list = self.get_string_split(line)
        ret_list = [self.get_value(i) for i in l_list]

        f_string = ("{}, " * len(ret_list))[:-2].format(*ret_list)

        return "return {}".format(f_string)

    def read_file(self,
                  fp,
                  space_count: int):
        spaces = 0
        with open(fp) as f:
            line = f.readline()
            self._string_list.extend(["from Script.Datatypes.Arrays import *",
                                      "from Script.Datatypes.Primitives import *",
                                      "from Script.PreBuilt import *",
                                      "from Script.Datatypes.Lists import *",
                                      "from Script.Datatypes.Matrices import *",
                                      "",
                                      ""])
            while line:
                curr_str = None
                line = line.strip()

                if line.startswith("METHOD"):
                    curr_str, m_name = self.method_line(line)
                elif line.startswith(tuple(self.starters.keys())):
                    curr_str = self.var_line(line, first=True)
                elif line.startswith(self.loop_starters):
                    curr_str = self.for_line(line)
                elif line.startswith("IF"):
                    curr_str = self.if_else_line(line, iff=True)
                elif line.startswith("ELIF"):
                    curr_str = self.if_else_line(line, eliff=True)
                elif line.startswith("ELSE"):
                    curr_str = self.if_else_line(line)
                elif line.startswith("BREAK"):
                    curr_str = "break"
                elif line.startswith("<<"):
                    curr_str = self.get_value(line)
                elif line.startswith("RETURN"):
                    curr_str = self.return_line(line)
                elif "=" in line:
                    curr_str = self.var_line(line)
                if curr_str:
                    curr_str = " " * spaces + curr_str
                    self._string_list.append(curr_str)

                if line.endswith("-->"):
                    spaces += space_count
                elif line.startswith("<--"):
                    spaces -= space_count

                line = f.readline()

    def compile(self, save_path):
        c = ["\n" + i for i in self._string_list]

        with open(save_path, "w") as file:
            file.writelines(c)
