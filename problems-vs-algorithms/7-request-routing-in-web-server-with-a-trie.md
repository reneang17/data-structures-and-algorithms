Build an autocomplete system with a Trie.
================

### Task
Build a router using a trie.


### Choices and reasoning and complexity of methods implemented.


Class RouteTrieNode

-  Individual insert have time complexity \(O(1\) and space complexity \(O(s\) where s is the size of the string inserted.

- Find simply hashes to make to its destination. Space complexity \(O(1\) and time complexity \(O(1\).

Class RouteTrie:
- Insert simply calls the TrieNode method for each part of the path. In the worst case, the time complexity is \(O(n*m*\) where n is the total number of paths in the Trie and the number of the path to be inserted, it is defined by using the Split_path method. The space complexity is O(m*s), where s is the longest part of the path. See
[referece](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014) for details.


Class Trie.
- Split_path method, has time complexity \(O(m\) where m is the number of parts of the path.
Space complexity is \(O(m*s\) where s is the longest part of the path.
- Add_handler simply calls Split_path and the insert TrieNode method. In the worst case, this gives a time complexity of \(O(n*m\) where n is the total number of paths in the Trie, so far, and m is the number of parts on the path inserted path. The space complexity is O(m*s), where s is the longest part of the path. See
![referece](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014) for details.
- Lookup method. First uses Split_path method, then employs the find method the relevant node and finally looks into its handler. Everything apart from the use Split_path method occurs on constant time/space, hence loop up has the same time/space complexity as that method.

More than 3 edge and normal cases tested.
