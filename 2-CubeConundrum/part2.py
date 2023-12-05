import re
from math import prod 

with open('data.txt', 'r') as file:
    games = file.read().split('\n')

pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')

def game_product(game):
    colour_min = {'red': 0, 'green': 0, 'blue': 0}
    matches = pattern.findall(game)
    for number, colour in matches:
        colour_min[colour] = max(int(number), colour_min[colour])

    return prod(colour_min.values())

if '__main__' == __name__:
    total_game_sum = sum(game_product(game) for game in games)
    print(total_game_sum)