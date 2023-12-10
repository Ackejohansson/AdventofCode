import os
import numpy as np
from collections import deque
    
dir = {
    "left": "-J7",
    "right": "-LF",
    "up": "|JL",
    "down": "|7F",
}

file = 'data.txt'
cwd = os.path.dirname(__file__)
file_path = os.path.join(cwd, file)

grid = np.array([list(line) for line in open(file_path).read().split("\n")])
m, n = grid.shape

def is_legal(i,j, direction, include_s):
    global m, n, dir
    if not (0 <= i < m and 0 <= j < n):
        return False
    if grid[i,j] in dir[direction]:
        return True
    if include_s and grid[i,j] == 'S':
        return True
    return False

        
i,j = np.where(grid == 'S')
si, sj  = i[0], j[0]

seen = {(si, sj)}
q = deque([(si, sj)])

while q:
    i, j = q.popleft()

    # Left 0,-1
    if (i, j-1) not in seen and is_legal(i,j,"left", True) and is_legal(i,j-1,"right", False):
        q.append((i,j-1))
        seen.add((i,j-1))
    
    # Right
    if (i, j+1) not in seen and is_legal(i,j,"right", True) and is_legal(i,j+1,"left", False):
        q.append((i,j+1))
        seen.add((i,j+1))
    # Up
    if (i-1, j) not in seen and is_legal(i,j,"up", True) and is_legal(i-1,j,"down", False):
        q.append((i-1,j))
        seen.add((i-1,j))

    # Down
    if (i+1, j) not in seen and is_legal(i,j,"down", True) and is_legal(i+1,j,"up", False):
        q.append((i+1,j))
        seen.add((i+1,j))
    print("Hello")

print(seen)
print(len(seen)//2)