Build an autocomplete system with a Trie.
================

### Task
Build a router using a trie.


### Choices and reasoning and complexity of methods implemented.


Class RouteTrieNode
-  Individual insert have time complexity \(O(1\) and space complexity \(O(m\) where m is the max length of the paths.
- Creating the complete Trie has, in the worst case, space complexity \(O(n*m\) where n is the number of times inserted and m is the max length of inserted strings, and time complexity equal to \(O(n\).
- Find simply hashes to make to its destination. Space complexity \(O(1\) and time complexity \(O(1\).

Class RouteTrie:
- Insert simply calls the TrieNode method.

Class Trie.
- Add_handler simply calls the insert TrieNode method.
- Lookup method. First, uses find to find the relevant node. Then, it looks into each of the p keys of the subnodes. Time  \(O(p\), space complexity \(O(1\).
- Split_path method, has time an space complexity \(O(m\) where m is the size of the path.

More than 3 edge and normal cases tested.
