# ddd - Lab2 - Variant 2

## group name and group member

- Name:
  - ddd

- Member
  - Wang Qihang:
    - id: 212320003
    - email: Wqhlw@hdu.edu.cn
  - Wang Zehao:
    - id: 212320005
    - email: 15029930122@163.com

## Project structure

DynamicArray.py -- includes class DynamicArray with methods add, length, __eq__ and __str__, class Iterator with __iter__ and __next__, and functions cons, remove, length, member, reverse, set, to_list, from_list, find, filter, map, reduce, iterator, empty, and concat.

test_DynamicArray.py -- unit and PBT tests for classes and functions in DynamicArray.py.

## contribution

Wang Qihang Completed the DynamicArray.py

Wang Zehao Completed the test_DynamicArray.py

## Changelog

- 13.04.2022 - 2
  - Wang Qihang upload DynamicArray.py
- 13.04.2022 - 1
  - Wang Zehao upload DynamicArray.py
- 13.05.2022 - 0
  - Initial

## Design notes

- Advantages of unittest:
  - Support automated testing
  - Secondary development is convenient
  - Organize test cases together by class

- Disadvantages of unittest:
  - Must be written in TestCase subclass
  - Must write test method
  - Difficult to expand

- Advantages of immutable tests:
  - Immutable algorithms reduces the complexity that mutable algorithms brings
  - Save memory
  - Copy and paste these operations are very simple to do
  - Traditional concurrency requires locking, but this data is inherently immutable, so concurrency is not needed

- Disadvantages of immutable tests:
  - Immutable algorithms require a separate object for each distinct value. 
