seeds, *blocks = open(0).read().split('\n\n')

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