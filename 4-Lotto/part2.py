import re

with open('4-Lotto/data.txt', 'r') as file:
    data = file.read().split('\n')

data = [row[10:] for row in data]

pattern = re.compile(r'\b[1-9]\d?\b')
ans = 0

test_data = [
    '41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    '13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    ' 1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    '41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    '87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    '31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    ]
# data = test_data

for row in data:
    left, right = row.split('|')
    left_matches = pattern.findall(left)
    right_matches = pattern.findall(right)
    matches = [left for left in left_matches if left in right_matches]
    if len(matches) >= 1:
        ans += pow(2, len(matches)-1)

   
print(ans)
data[0]