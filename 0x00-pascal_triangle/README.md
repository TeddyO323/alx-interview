# 0x00. Pascal's Triangle

**Project Score:** 100%

Feel free to share your thoughts and experiences with the project. If you have any feedback or questions, please let me know! Your engagement and feedback are highly appreciated.


## Algorithm
**Language:** Python

## Tasks

### 0. Pascal's Triangle
**mandatory**

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

**Repo:**
- GitHub repository: `alx-interview`
- Directory: `0x00-pascal_triangle`
- File: `0-pascal_triangle.py`
```