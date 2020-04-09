Build an autocomplete system with a Trie.
================

### Task
Build an autocomplete function using a Trie.


### Choices and reasoning and complexity of methods implemented.


Class TrieNode.
-  Individual insert have time complexity \(O(1\) and space complexity \(O(m\) where m is the max length of the strings.
- Creating the complete Trie has, in the worst case, space complexity \(O(n*m\) where n is the number of times inserted and m is the max length of inserted strings, and time complexity equal to \(O(n\).

Class Trie.
- Insert calls the insert TrieNode method.
- Find simply hashes to make to its destination. Space complexity \(O(1\) and time complexity \(O(1\).
- Suffixes method. First, uses find to search the relevant node. Then, it looks into each of the p keys of such node. Time  \(O(p\), space complexity \(O(1\).


More than 3 edge and normal cases tested.
