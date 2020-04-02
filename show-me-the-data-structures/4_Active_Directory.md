Active Directories
================

### Task
Search active users in groups and subgroups.

### Choices and reasoning

- Modified Group class to store users in a binary tree, adding O\(m_files\) time and space complexity.
- Function search recursively in subfolders. Time complexity O\(O_subfolder log(m_files) \). Space complexity is O\(1\).
- Tested, including edge cases.

### Complexity

- Big O, time complexity of search: O\(n_subfolder * log(m_files) \). Where n is the length of input string.

- Big O, space complexity of searching is O\(1\), and of creating the groups with subgroups,
is O\(n_folders * log(m_files)\).
