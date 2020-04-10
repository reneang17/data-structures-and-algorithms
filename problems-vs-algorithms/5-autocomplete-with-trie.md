Build an autocomplete system with a Trie.
================

### Task
Build an autocomplete function using a Trie.


### Choices and reasoning and complexity of methods implemented.


Class TrieNode.
-  Individual insert have time complexity \(O(1\) and space complexity \(O(1\) to insert a single character.
- Suffixes method. First, uses find to search the relevant node. Then, it looks into each of the p keys of such node. In the worst case, due to this second step, it has to traverse all the nodes below giving it time complexity and auxilary space complexity  \(O(n*m\) where n is total of (sub)nodes and m is the size of the prefix.

Class Trie.
- Insert calls the insert TrieNode method for each character of relevant word. In the worst case, the time complexity is \(O(n*m\) where n is the total number of words in the Trie, so far, and m is the word length. The space complexity is O(m). See
[referece](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)

- Find simply hashes to make to its destination. Space complexity \(O(1\) and time complexity \(O(1\).

More than 3 edge and normal cases tested.
