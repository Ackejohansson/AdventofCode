import os
from math import gcd

file_name = "data.txt"
dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, file_name)

with open(file_path, 'r') as file:
    steps, _, *rest = file.read().splitlines()

network = {}
for line in rest:
    pos, target = line.split(" = ")
    network[pos] = target[1:-1].split(", ")

keys = [key for key in network if key.endswith("A")]

cycles = []
for position in keys:
    step_count = 0
    while not position.endswith("Z"):
        position = network[position][0 if steps[0] == "L" else 1]
        
        steps = steps[1:] + steps[0]
        step_count +=1
    cycles.append(step_count)

result = 1
for number in cycles:
    result = number * result // gcd(number, result)

print(result)


