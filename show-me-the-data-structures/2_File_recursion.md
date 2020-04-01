File Recursion
================


### Choices and reasoning

Recurrent function:
- List of files in current directory
- List subdirs in current directory
- Calls itself for each folder
- Adds directories find in present and previous Calls
- Return files
- Tested, including edge cases. 

### Complexity

- Big O, time complexity: \(O(n * m)\), where n is the length of recursion stack and
the maximum number of files in a given folder.

- Big O, space complexity: \(O(m)\), where m is total number of files.
