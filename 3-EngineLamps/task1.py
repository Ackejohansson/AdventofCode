import numpy as np

with open('data.txt', 'r') as file:
    lines = file.read().split('\n')


n = len(lines)
m = len(lines[0])
ans = 0

def is_symbol(i, j):
    if not (0 <= i < n and 0 <= j < m):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()

for i, line in enumerate(lines):
    j = 0
    while j < m:
        # Loop to digit
        if not line[j].isdigit():
            j += 1
            continue
        
        # Find the entire number
        start = j
        num = ""
        while j < m and line[j].isdigit():
            num += line[j]
            j+=1
        number = int(num)

        # Check Left-right
        if is_symbol(i, start-1) or is_symbol(i, j):
            ans += number
            continue
        
        # Check above and under
        for k in range(start-1, j+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                ans += number
                continue

print(ans)