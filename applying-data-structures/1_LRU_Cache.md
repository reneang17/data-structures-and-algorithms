Least recurrent used
================

### Task
Implement using only O(1) time complexity.

### Choices and reasoning

- Hash table to save keys and values.
- Cache is implement with a linked, each node holding introduced keys,
and  are order according to the use, with the head node represent the least recurrent key.
- To avoid having to iterate over loop over linked list, key and nodes are
store in another hash table. This way we can re-order the linked list in constant time.
- Tested, including edge cases. 

### Complexity

- Big O, time complexity: \(O(1)\)

- Big O, space complexity: \(O(n)\). where n is the capacity of the hash tables.
