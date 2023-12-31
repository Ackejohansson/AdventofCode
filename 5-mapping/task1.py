import os
file_name = "data.txt"
dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, file_name)

with open(file_path, 'r') as file:
    seeds, *blocks = file.read().split('\n\n')

seeds = list(map(int, seeds.split(":")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
        
    new = []
    for seed in seeds:
        for a, b, c in ranges:
            if seed in range(b, b+c):
                new.append(seed-b+a)
                break
        else:
            new.append(seed)
    seeds = new

print(min(seeds))