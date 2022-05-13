import math
import copy


class DynamicArray:
    def __init__(self, capacity=10, factor=1):
        self.capacity = capacity
        self.factor = factor
        self.array_element = []
        self.element_index = 0

    def __str__(self):
        return str(self.array_element[:])

    def __eq__(self, other):
        len1 = len(self.array_element)
        len2 = len(other.array_element)
        if len1 != len2:
            return False
        elif len1 == 0:
            return True
        for i, j in zip(self, other):
            if i != j:
                return False
        return True


def cons(lst, element):
    tmp = copy.deepcopy(lst)
    tmp.array_element.append(element)
    return tmp


def remove(lst, pos):
    if pos < 0 or pos >= len(lst):
        raise Exception('The location accessed is not in the array!')
    tmp = DynamicArray()
    for i, _ in enumerate(lst):
        if i != pos:
            tmp.array_element.append(_)
    return tmp


def length(lst):
    return len(lst.array_element)


def member(lst, element):
    for _ in lst.array_element:
        if element == _:
            return True
    return False


def from_list(lst1):
    tmp = DynamicArray()
    for _ in lst1:
        tmp.array_element.append(_)
    return tmp


def reverse(lst):
    tmp = []
    for _ in lst:
        tmp.append(_)
    return from_list(tmp[::-1])


def to_list(lst):
    res = []
    res.extend(lst.array_element)
    res.reverse()
    return res


def find(lst, f):
    for _ in lst:
        if f(_):
            return True
    return False


def filter(lst, f):
    tmp = DynamicArray()
    for ele in lst.array_element:
        if f(ele) is True:
            tmp.array_element.append(ele)
    size = len(tmp.array_element)
    factor = tmp.factor
    tmp.capacity = size * factor
    return tmp


def map(lst, f):
    tmp = DynamicArray()
    tmp.capacity = lst.capacity
    for ele in lst.array_element:
        tmp.array_element.append(f(ele))
    return tmp


def reduce(lst, f, initial_state):
    state = initial_state
    tmp = DynamicArray()
    tmp.capacity = lst.capacity
    for ele in lst.array_element:
        tmp.array_element.append(f(ele, state))
    return tmp


def iterator_element(lst):
    tmp = DynamicArray()
    tmp.capacity = lst.capacity
    tmp.array_element.extend(lst.array_element)
    return tmp


def next_element(lst):
    if lst.element_index > len(lst.array_element):
        print("stop iterator")
        return 0
    size = len(lst.array_element) - 1
    tmp = lst.array_element[size - lst.element_index]
    lst.element_index += 1
    return tmp


def empty():
    return DynamicArray()


def concat(lst1, lst2):
    tmp = DynamicArray()
    len1 = len(lst1.array_element)
    len2 = len(lst2.array_element)
    factor = tmp.factor
    tmp.capacity = (len1 + len2) * factor
    element = lst2.array_element
    tmp.array_element.extend(element)
    element = lst1.array_element
    tmp.array_element.extend(element)
    return tmp
