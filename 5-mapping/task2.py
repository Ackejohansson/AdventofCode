input, *blocks = open(0).read().split('\n\n')

input = list(map(int, input.split(":")[1].split()))

seeds = []
for i in range(0, len(input), 2):
    seeds.append((input[i], input[i]+input[i+1]))
    
exit(0)
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