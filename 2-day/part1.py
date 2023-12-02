import re

colour_map = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open('2-day/data.txt', 'r') as file:
    data = file.read().split('\n')

pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')

def game_config(game):
    matches = pattern.findall(game)
    for number, colour in matches:
        if int(number) > colour_map[colour]:
            return False
    return True

if '__main__' == __name__:
    game_id_sum = 0
    for index, game in enumerate(data):
        if game_config(game):
            game_id_sum += index + 1
            
    # print(data)
    print(game_id_sum)