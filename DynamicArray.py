import copy


class DynamicArray:
    def __init__(self, capacity=10, factor=2):
        self.__capacity = capacity
        self.__factor = factor
        self.__chunk = [None] * self.__capacity
        self.__element_index = -1
        self.__length = 0

    def length(self):
        return self.__length

    def add(self, ele):
        if self.__length == self.__capacity:
            new_chunk = int(self.__capacity * self.__factor) - self.__capacity
            self.__chunk += [None] * new_chunk
            self.__capacity = self.__capacity + new_chunk
        self.__chunk[self.__length] = ele
        self.__length += 1

    def __str__(self):
        return str(self.__chunk[:self.__length])

    def __eq__(self, other):
        len1 = self.length()
        len2 = other.length()
        if len1 != len2:
            return False
        elif len1 == 0:
            return True
        for i, j in zip(self, other):
            if i != j:
                return False
        return True

    def __iter__(self):
        return Iterator(self.__chunk, self.__length)


class Iterator(object):
    def __init__(self, lst, lng):
        self.__chunk = lst
        self.__length = lng
        self.__element_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__element_index += 1
        if self.__element_index >= self.__length:
            raise StopIteration()
        return self.__chunk[self.__element_index]


def cons(lst, ele):
    tmp = copy.deepcopy(lst)
    tmp.add(ele)
    return tmp


def remove(lst, pos):
    if pos < 0 or pos >= lst.length():
        raise Exception('The location accessed is not in the array!')
    tmp = DynamicArray(capacity=len(lst1))
    for i, _ in enumerate(lst):
        if i != pos:
            tmp.add(_)
    return tmp


def length(lst):
    return lst.length()


def member(lst, element):
    for _ in lst:
        if element == _:
            return True
    return False


def from_list(v):
    tmp = DynamicArray()
    for _ in v:
        tmp.add(_)
    return tmp


def reverse(lst):
    tmp = []
    for _ in lst:
        tmp.append(_)
    return from_list(tmp[::-1])


def to_list(lst):
    res = []
    for _ in lst:
        res.append(_)
    return res


def find(lst, f):
    for _ in lst:
        if f(_):
            return True
    return False


def filter(f, lst):
    res = DynamicArray(capacity=lst.length())
    for k in lst:
        if f(k):
            res.add(k)
    return res


def map(f, *iters):
    res = DynamicArray()
    for args in zip(*iters):
        res.add(f(*args))
    return res


def reduce(function, lst, initializer=None):
    it = iterator(lst)
    if initializer is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no "
                            "initial value") from None
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


def iterator(lst):
    return iter(lst)


def empty():
    return DynamicArray(capacity=0)


def concat(lst1, lst2):
    res = DynamicArray(capacity=lst1.length()+lst2.length())
    for k in lst1:
        res.add(k)
    for k in lst2:
        res.add(k)
    return res


def set(lst, p, v):
    if v is not None and type(v) != int:
        raise Exception('Input data must be int or None')
    if p < 0 or p >= lst.length():
        raise Exception('The location accessed is not in the array!')
    res = DynamicArray(capacity=lst.length())
    for idx, i in enumerate(lst):
        if p == idx:
            res.add(v)
        else:
            res.add(i)
    return res
