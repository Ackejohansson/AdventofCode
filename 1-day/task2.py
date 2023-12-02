import re

number_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# ?= for overlapping words
number_regex = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))')


def find_number(line):
    matches = number_regex.findall(line)
    numeric_values = [number_map[match] if not match.isdigit() else int(match) for match in matches]
    return numeric_values[0]*10+numeric_values[-1]

if '__main__' == __name__:
    sum = 0
    for line in data:
        sum += find_number(line)
    print(sum)