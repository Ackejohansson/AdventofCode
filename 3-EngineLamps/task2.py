with open('data.txt', 'r') as file:
    lines = file.read().split('\n')

n = len(lines)
m = len(lines[0])
ans = 0
# Create 2d list of lists to
gear = [[[] for _ in range(m)] for _ in range(n)]

def is_symbol(i, j, num):
    if not (0 <= i < n and 0 <= j < m):
        return False
    if lines[i][j] == '*':
        gear[i][j].append(num)

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
        is_symbol(i, start-1, number) or is_symbol(i, j, number)
        
        # Check above and under
        for k in range(start-1, j+1):
            is_symbol(i-1, k, number) or is_symbol(i+1, k, number)

for i in range(n):
    for j in range(m):
        numbers = gear[i][j]
        if len(numbers) == 2:
            ans += numbers[0]*numbers[1]

print(ans)