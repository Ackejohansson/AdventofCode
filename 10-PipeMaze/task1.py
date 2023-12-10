import os
import numpy as np
from collections import deque
directions = ["left", "right", "up", "down"]
    
dir = {
    "left":"-LF",
    "right":"a",
    "up":"L",
    "down":"-"
}
pipes = '| - L J 7 F . '

file = 'test.txt'
cwd = os.path.dirname(__file__)
file_path = os.path.join(cwd, file)

grid = np.array([list(line) for line in open(file_path).read().split("\n")])
m, n = grid.shape

def is_legal(i,j, direction):
    if not (0 <= i < m and 0 <= j < n):
        return False
    for direction in directions:
        # go
        grid[i,j] in dir
        # recieve



        
i,j = np.where(grid == 'S')
sr, sj  = i[0], j[0]

seen = {(sr, sj)}
q = deque([sr, sj])

while q:
    i, j = q.popleft()


