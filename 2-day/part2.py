import re
from math import prod 

with open('2-day/data.txt', 'r') as file:
    games = file.read().split('\n')

pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')

def check_game(game):
    colour_min = {
        'red': 0,
        'green': 0, 
        'blue': 0,
    }
    matches = pattern.findall(game)
    for number, colour in matches:
        if int(number) > colour_min[colour]:
            colour_min[colour] = int(number)

    return prod(colour_min.values())

if '__main__' == __name__:
    total_game_sum = sum(check_game(game) for game in games)
    print(total_game_sum)