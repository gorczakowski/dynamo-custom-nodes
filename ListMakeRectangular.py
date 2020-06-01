# Created by Krzysztof Gorczakowski, 2020
# https://github.com/gorczakowski

def toList(obj):
    if isinstance(obj, list):
        return obj
    else:
        return [obj]

def lengthen(obj, length, f_fill):
    obj_len = len(obj)
    if obj_len == length:
        return obj
    else:
        if f_fill:
            obj[:0] = [obj[0]] * (length - obj_len)
            return obj
        else:
            obj[obj_len:] = [obj[-1]] * (length - obj_len)
            return obj

input_lists = IN[0]
f_fill = IN[1]

lsts = [toList(i) for i in input_lists]
max_len = max(len(lst) for lst in lsts)

try:
    OUT = [lengthen(lst, max_len, f_fill) for lst in lsts]
except Exception as e:
    OUT = str(e)
