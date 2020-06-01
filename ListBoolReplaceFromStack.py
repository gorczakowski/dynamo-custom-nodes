# Created by Krzysztof Gorczakowski, 2020
# https://github.com/gorczakowski

def toList(obj):
    if isinstance(obj, list):
        return obj
    else:
        return [obj]

def trypop(lst, alt_item):
    try:
        return lst.pop(0)
    except:
        return alt_item
    
def tryindex(lst, index):
    try:
        return lst[index]
    except:
        return False

lst = toList(IN[0])
mask = toList(IN[1])
stack = toList(IN[2])

try:
    OUT = [trypop(stack, lst[i]) if tryindex(mask, i) else lst[i] for i in range(len(lst))]
except Exception as e:
    OUT = str(e)
