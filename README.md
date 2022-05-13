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

## contribution

- Wang Qihang Completed the DynamicArray.py

- Wang Zehao Completed the test_DynamicArray.py

## Changelog

- 13.04.2022 - 2
  - Wang Qihang upload DynamicArray.py.
- 13.04.2022 - 1
  - Wang Zehao upload DynamicArray.py.
- 13.05.2022 - 0
  - Initial.

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
  - Traditional concurrency requires locking, but this data is inherently immutable

- Disadvantages of immutable tests:
  - Immutable algorithms require a separate object for each distinct value.
