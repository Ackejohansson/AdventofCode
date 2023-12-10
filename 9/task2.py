import numpy as np

def extrapolate(numbers):
    if np.all(numbers == 0):
        return 0
    diff = extrapolate(numbers[1:] - numbers[:-1])
    return numbers[-1] + diff

total = 0
for line in open(0):
    numbers = np.array(list(map(int, line.split())))
    total += extrapolate(numbers)
print(total)