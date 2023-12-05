import re

with open('data.txt', 'r') as file:
    data = file.read().split('\n')
    data = [row[10:] for row in data]

ans = 0
pattern = re.compile(r'\b[1-9]\d?\b')

for row in data:
    left, right = row.split('|')
    left_matches, right_matches = pattern.findall(left), pattern.findall(right)
    array = [left for left in left_matches if left in right_matches]
    if len(array) >= 1:
        ans += pow(2, len(array)-1)
   
print(ans)
data[0]