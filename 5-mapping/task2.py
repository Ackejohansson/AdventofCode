input, *blocks = open(0).read().split('\n\n')
input = list(map(int, input.split(":")[1].split()))

seeds = []
for i in range(0, len(input), 2):
    seeds.append((input[i], input[i]+input[i+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    
    new = []
    while seeds:
        ss, se = seeds.pop()
        for a, b, c in ranges:
            os = max(ss, b)
            oe = min(se, b+c)
            if os < oe:
                new.append((os-b+a, oe-b+a))
                if ss < os:
                    seeds.append((ss, os))
                if se > oe:
                    seeds.append((oe, se))
                break
        else:
            new.append((ss, se))
    seeds = new

print(min(seeds)[0])