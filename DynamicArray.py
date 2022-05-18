class DynamicArray:
    """ Immutable dynamic array Implementation """
    
    def __init__(self, capacity=10, factor=2):
        """
            Create an instance of DynamicArray.
            :param capacity
            :param factor
        """
        self.__capacity = capacity
        self.__factor = factor
        self.__chunk = [None] * self.__capacity
        self.__element_index = -1
        self.__length = 0

    def length(self):
        return self.__length

    def add(self, ele):
        """ add element """
        if self.__length == self.__capacity:
            new_chunk = int(self.__capacity * self.__factor) - self.__capacity
            self.__chunk += [None] * new_chunk
            self.__capacity = self.__capacity + new_chunk
        self.__chunk[self.__length] = ele
        self.__length += 1

    def __str__(self):
        return str(self.__chunk[:self.__length])

    def __eq__(self, other):
        """ The array whether equals other array. """
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
    """ An iterator object of DynamicArray. """
    
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
    """ Insert a value at start of array. """
    import copy
    tmp = copy.deepcopy(lst)
    tmp.add(ele)
    return tmp


def remove(lst, pos):
    """ Remove value at position p of array. """
    if pos < 0 or pos >= lst.length():
        raise Exception('The location accessed is not in the array!')
    tmp = DynamicArray()
    for i, _ in enumerate(lst):
        if i != pos:
            tmp.add(_)
    return tmp


def length(lst):
    """ Return the length of array. """
    return lst.length()


def member(lst, element):
    """ Determines whether the given value is a member of array. """
    for _ in lst:
        if element == _:
            return True
    return False


def from_list(v):
    """ Transform a list to an array. """
    tmp = DynamicArray()
    for _ in v:
        tmp.add(_)
    return tmp


def reverse(lst):
    """ Reverse array. """
    tmp = []
    for _ in lst:
        tmp.append(_)
    return from_list(tmp[::-1])


def to_list(lst):
    """ Transform an array to a list. """
    res = []
    for _ in lst:
        res.append(_)
    return res


def find(lst, f):
    """ Find element by specific predicate. """
    for _ in lst:
        if f(_):
            return True
    return False


def filter(f, lst):
    """ Filter an array by specific predicate. """
    res = DynamicArray()
    for k in lst:
        if f(k):
            res.add(k)
    return res


def map(f, *iters):
    """
         Apply the function to each instance of dynamiccarray and produce results.
         If other instance parameters are passed,
         the function must accept so many parameters and apply them to items in all instances in parallel.
         For multiple instances, the mapping stops when the shortest instance runs out.
    """
    res = DynamicArray()
    for args in zip(*iters):
        res.add(f(*args))
    return res


def reduce(function, lst, initializer=None):
    """
        Apply function of two arguments cumulatively to the items of the
                array, from left to right, to reduce the array to a single value.
        :param function: Callable.
        :param lst: array.
        :param initial: If the optional initializer is present, it is placed
            before the items of the array in the calculation, and serves as
            a default when the array is empty. If initializer is not given
            and array contains only one item, the first item is returned.
    """
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
    """ Return an iterator of DynamicArray. """
    return iter(lst)


def empty():
    """ Return an empty instance of DynamicArray """
    return DynamicArray()


def concat(lst1, lst2):
    """ Concat two array. """
    res = DynamicArray()
    for k in lst1:
        res.add(k)
    for k in lst2:
        res.add(k)
    return res


def set(lst, p, v):
    """ Add an element into the array at specified position. """
    if v is not None and type(v) != int:
        raise Exception('Input data must be int or None')
    if p < 0 or p >= lst.length():
        raise Exception('The location accessed is not in the array!')
    res = DynamicArray()
    for idx, i in enumerate(lst):
        if p == idx:
            res.add(v)
        else:
            res.add(i)
    return res
