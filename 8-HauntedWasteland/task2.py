import os

file_name = "data.txt"
dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, file_name)

with open(file_path, 'r') as file:
    steps, _, *rest = file.read().splitlines()

network = {}
for line in rest:
    pos, target = line.split(" = ")
    network[pos] = target[1:-1].split(", ")

key = "AAA"
step_count = 0

while key != "ZZZ":
    key = network[key][0 if steps[0] == "L" else 1]
    
    steps = steps[1:] + steps[0]
    step_count +=1

print(step_count)