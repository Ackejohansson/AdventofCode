import os
import numpy as np

file = 'data.txt'
dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, file)

with open(file_path, 'r') as file:
    data = file.read().splitlines()
    data = np.array([list(line) for line in data])

empty_cols = np.all(data == '.', axis=0)
empty_rows = np.all(data == '.', axis=1)
rows, cols = np.where(data == '#')
points = list(zip(rows, cols))

dist = 0
# Minus 1 since the empty cols are already added from the abs(i-i2)
scale = 1000000 - 1

for index, (i,j) in enumerate(points):
    for i2, j2 in points[:index]:
        row_range = slice(min(i, i2), max(i, i2))
        col_range = slice(min(j, j2), max(j, j2))
        empty_space = sum(empty_cols[col_range]) + sum(empty_rows[row_range])
        
        dist += np.abs(i-i2) + np.abs(j-j2) + scale*(empty_space)

print(dist)