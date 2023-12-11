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

keys = [key for key in network if key.endswith("A")]
step_count = 0


while not all([key.endswith("Z") for key in keys]):
    for i, key in enumerate(keys):
        keys[i] = network[key][0 if steps[0] == "L" else 1]
    
    steps = steps[1:] + steps[0]
    step_count +=1

print(step_count)