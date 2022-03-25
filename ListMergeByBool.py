# Created by Krzysztof Gorczakowski, 2022
# https://github.com/gorczakowski

def to_list(obj):
	return obj if hasattr(obj, '__iter__') else list(obj)

list1 = to_list(IN[0])
list2 = to_list(IN[1])
bools = to_list(IN[2])

l = min(len(list1), len(list2), len(bools))

OUT = [list1[i] if bools[i] else list2[i] for i in range(l)]