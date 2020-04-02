Union and intersection of two linked lists.
================


### Choices and reasoning
Generally, I used binary trees to eliminate duplicates and searching.

## Union:

- Empty linked into binatry tree. O\(n_1\) in space and O\( log(n_1)\) in time.
- Empty the other linked list into binary tree. O\(n_2\) in space and O\( log(n_2)\) in time.
- Flatten binary tree and empty it into linked list. Space and time O\(n\), where n = n_1+n_2.
- Tested, including edge cases.

### Complexity

- Big O, time complexity: \(O(lon(n))\)

- Big O, space complexity: \(O(n)\)

## Intersection:

- Empty linked into binatry tree. O\(n_1\) in space and O\( log(n_1)\) in time.
- Empty linked into binatry tree. O\(n_2\) in space and O\( log(n_2)\) in time.
- Iterate over one tree checking that nodes are share by both trees. Time O\(n log(n)\).
Empty into linked list. O\(n\) in space, where n = n_1+n_2.
- Tested, including edge cases.

### Complexity

- Big O, time complexity: \(O(n lon(n))\).

- Big O, space complexity: \(O(n)\)
