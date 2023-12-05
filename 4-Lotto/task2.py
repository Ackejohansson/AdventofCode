import re
import numpy as np

ans = 0

# Load data
file_path = 'data.txt'
with open(file_path, 'r') as file:
    file = file.read().split('\n')
data = np.array([row[10:] for row in file])


# Split the data at |
split = np.array(np.char.split(data, '|').tolist())
left, right = split[:,0], split[:, 1]

# Match with pattern
pattern = re.compile(r'\b[1-9]\d?\b')
left_matches =  [pattern.findall(row) for row in left]
right_matches = [pattern.findall(row) for row in right]

# Compute the card number array
nr_of_cards = np.ones(len(data), dtype=int)
for i in range(0, len(data)):
    nr_matches = len(set(left_matches[i]) & set(right_matches[i]))
    nr_of_cards[i+1:min(i+1+nr_matches, len(data))] += nr_of_cards[i]

ans = sum(nr_of_cards)
print(ans)