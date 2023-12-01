import re

number_map = {
    'zero': 0,
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

with open('1-day/data.txt', 'r') as file:
    data = file.read().split('\n')


number_regex = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))')


def find_number(line):
    number_matches = number_regex.findall(line)
    filtered_matches = [match for match in number_matches if match in number_map or match.isdigit()]
    numeric_values = [number_map[match] if not match.isdigit() else int(match) for match in filtered_matches]
    return numeric_values[0]*10+numeric_values[-1]

sum=0
for line in data:
    numbers = find_number(line)
    sum += numbers
print(sum)