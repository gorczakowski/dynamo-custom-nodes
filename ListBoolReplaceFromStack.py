# Created by Krzysztof Gorczakowski, 2020
# https://github.com/gorczakowski

def to_list(obj):
	return obj if hasattr(obj, '__iter__') else list(obj)

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

lst = to_list(IN[0])
mask = to_list(IN[1])
stack = to_list(IN[2])

try:
    OUT = [trypop(stack, lst[i]) if tryindex(mask, i) else lst[i] for i in range(len(lst))]
except Exception as e:
    OUT = str(e)
