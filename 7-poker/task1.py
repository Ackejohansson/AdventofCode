strength_map = {"T":"A", "J":"B", "Q":"C", "K":"D", "A":"E"}

def classify(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if 2 in counts:
        if counts.count(2) == 4:
            return 2
        return 1
    return 0
    
def strength(hand):
    return classify(hand), [strength_map.get(char, char) for char in hand]


plays = []
for line in open(0):
    hand, bet = line.split()  
    plays.append((hand, int(bet)))

plays.sort(key=lambda play:strength(play[0]))

ans = 0
for rank, (hand, value) in enumerate(plays, 1):
    ans += rank * value

print(ans)