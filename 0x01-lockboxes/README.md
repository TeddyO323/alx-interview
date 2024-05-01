# Lockboxes Project Overview

## Project Details
- **Title:** Lockboxes
- **Technology:** Algorithm, Python
- **Weight:** 1
- **Start Date:** Apr 29, 2024, 6:00 AM
- **End Date:** May 3, 2024, 6:00 AM
- **Checker Release Date:** Apr 30, 2024, 6:00 AM
- **Auto Review:** Will be launched at the deadline

## Must Know
To successfully complete this project, you'll need a solid grasp of the following concepts and resources:

### Concepts Needed:
1. **Lists and List Manipulation:**
   - Accessing, iterating, and modifying lists dynamically.
   - Resources: [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

2. **Graph Theory Basics:**
   - Traversal algorithms like Depth-First Search or Breadth-First Search.
   - Resources: [Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)

3. **Algorithmic Complexity:**
   - Time and space complexity analysis for efficient algorithms.
   - Resources: [Big O Notation](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)

4. **Recursion:**
   - Recursive approaches for traversing through boxes and keys.
   - Resources: [Recursion in Python](https://realpython.com/python-recursion/)

5. **Queue and Stack:**
   - Utilizing queues and stacks for BFS or DFS algorithms.
   - Resources: [Python Queue and Stack](https://www.geeksforgeeks.org/queue-in-python/)

6. **Set Operations:**
   - Using sets to track visited boxes and available keys.
   - Resources: [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

By understanding and applying these concepts, you'll be equipped to develop an efficient solution for the Lockboxes project, showcasing your algorithmic and Python programming skills.

## Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?v=V8DGdPkBBxg)

## Requirements
### General
- Editors: vi, vim, emacs
- Environment: Ubuntu 20.04 LTS with python3 (version 3.4.3)
- File Format: Unix newline endings
- File Header: #!/usr/bin/python3 as the first line
- Documentation: Required for your code
- Style Guide: PEP 8 version 1.7.x
- Executability: All files must be executable

## Tasks
### Lockboxes
You have n locked boxes numbered from 0 to n - 1, each potentially containing keys to other boxes. Write a method to determine if all boxes can be opened.

**Prototype:** `def canUnlockAll(boxes)`
- `boxes`: List of lists
- A key with the same number as a box opens that box
- All keys are positive integers
- Return True if all boxes can be opened, else return False

### Example
```python
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

### Repository Details
- GitHub Repository: alx-interview
- Directory: 0x01-lockboxes
- File: 0-lockboxes.py
