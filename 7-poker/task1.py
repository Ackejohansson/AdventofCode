strength_map = {"J":"A", "Q":"B", "K":"C", "A":"D"}

def classify(hand):
    pass

def strength(hand):
    # Want to return 
    # the type and 
    # alpabetical order of the hand based on strength
    return classify(hand), [strength.get(char, char) for char in hand]


plays = []
for line in open(0):
    hand, bet = line.split()  
    plays.append((hand, int(bet)))

plays.sort(key=lambda play:strength(play[0]))
