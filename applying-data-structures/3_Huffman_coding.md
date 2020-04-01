Huffman coding
================

### Task
Implement huffman coding and decoding.

### Choices and reasoning

- Make hash table of characters and frequencies O\(m\) space and O\(m\) time, where m is the
 number of characters in the input string.
- Sort frequencies O\(log(m\)\)
- Form stack of pairs (char ,freq \). O\(m\) in time and space.
- From huffman tree iteratively poping the stack. Time complexity is O\(m^2\) because in the worst case
 the stack has to be emptied and filled at each iteration. Space complexity O\(m\).
- Making codes, depth first search. Space complexity is O\(m^2\). Time complexity is O\(m\).
- Decoding. Time complexity O\(m^2\). Space complexity O\(1\).
- Tested, including edge cases. 

### Complexity

- Big O, time complexity: O\(n^2\). Where n is the length of input string, everything else is subleading.

- Big O, space complexity: O\(m^2\) to make the codes, everythin else is subleading.
