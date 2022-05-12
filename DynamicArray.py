import math


class DynamicArray:
    def __init__(self, capacity=64, load_factor=2):
        self.capacity = capacity
        self.load_factor = load_factor
        self.array_node = []
        self.pos = 0

    def __str__(self):
        """for str() implementation for printing"""
        deli = ", "
        res = ""
        if len(self.array_node) != 0:
            nodes = self.array_node[::-1]
            res = deli.join(map(str, nodes))
        return "[" + res + "]"

    def __eq__(self, other):
        """prove that two DynamicArray are same"""
        len1 = len(self.array_node)
        len2 = len(other.array_node)
        if len1 != len2:
            return False
        else:
            if len1 == 0:
                return True
            for i in range(len1):
                node1 = self.array_node[i]
                node2 = other.array_node[i]
                flag1 = ((type(node1) == int
                          or type(node1) == float)
                         and math.isnan(node1))
                flag2 = ((type(node2) == int
                          or type(node2) == float)
                         and math.isnan(node2))
                if flag1 is True and flag2 is True:
                    continue
                if self.array_node[i] != other.array_node[i]:
                    return False
            return True


def cons(a, b):
    if isinstance(b, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    capacity = b.capacity
    load_factor = b.load_factor
    if len(b.array_node) == b.capacity:
        capacity = b.capacity * load_factor
    dynamicArray.capacity = capacity
    dynamicArray.load_factor = load_factor
    dynamicArray.array_node.extend(b.array_node)
    dynamicArray.array_node.append(a)
    return dynamicArray


def remove(a, b):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    c = (type(b) == int or type(b) == float) and math.isnan(b)
    for ele in a.array_node:
        if c is True and math.isnan(ele):
            continue
        elif ele != b:
            dynamicArray.array_node.append(ele)
    dynamicArray.capacity = a.capacity
    return dynamicArray


def length(a):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    return len(a.array_node)


def isMember(a, b):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    nan_flag = (type(b) == int or type(b) == float) and math.isnan(b)
    for ele in a.array_node:
        if ele == b:
            return True
        elif nan_flag and math.isnan(ele):
            return True
    return False


def reverse(a):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    tem_node = a.array_node
    tem_node.reverse()
    dynamicArray.array_node = tem_node
    dynamicArray.capacity = a.capacity
    return dynamicArray


def to_list(a):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    result = []
    result.extend(a.array_node)
    result.reverse()
    return result


def from_list(a):
    if isinstance(a, list) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    node = []
    node.extend(a)
    node.reverse()
    # the original list in the DynamicArray is reversed
    # so, when we get a list to the DynamicArray
    # we should reverse it.
    dynamicArray.array_node.extend(node)
    dynamicArray.capacity = len(a) * dynamicArray.load_factor
    return dynamicArray


def find(a, f):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    result = []
    for ele in a.array_node:
        if f(ele) is True:
            result.append(ele)
    result.reverse()
    return result


def filter_the_value(a, f):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    for ele in a.array_node:
        if f(ele) is True:
            dynamicArray.array_node.append(ele)
    siz = len(dynamicArray.array_node)
    factor = dynamicArray.load_factor
    dynamicArray.capacity = siz * factor
    return dynamicArray


def map_the_value(a, f):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    dynamicArray.capacity = a.capacity
    for ele in a.array_node:
        dynamicArray.array_node.append(f(ele))
    return dynamicArray


def reduce(a, f, initial_state):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    state = initial_state
    dynamicArray = DynamicArray()
    dynamicArray.capacity = a.capacity
    for ele in a.array_node:
        dynamicArray.array_node.append(f(ele, state))
    return dynamicArray


def iterator_element(a):
    if isinstance(a, DynamicArray) is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    dynamicArray.capacity = a.capacity
    dynamicArray.array_node.extend(a.array_node)
    return dynamicArray


def next_element(a):
    if a.pos > len(a.array_node):
        print("stop iterator")
        return 0
    siz = len(a.array_node) - 1
    tmp = a.array_node[siz - a.pos]
    a.pos += 1
    return tmp


def empty(a):
    return DynamicArray()


def concat(a, b):
    flag1 = isinstance(a, DynamicArray)
    flag2 = isinstance(b, DynamicArray)
    if flag1 is False or flag2 is False:
        print("Please input the correct DynamicArray object.")
        return DynamicArray()
    dynamicArray = DynamicArray()
    len1 = len(a.array_node)
    len2 = len(b.array_node)
    factor = dynamicArray.load_factor
    dynamicArray.capacity = (len1 + len2) * factor
    node = b.array_node
    dynamicArray.array_node.extend(node)
    node = a.array_node
    dynamicArray.array_node.extend(node)
    return dynamicArray
