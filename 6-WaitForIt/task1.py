import numpy as np
from math import prod

time = np.array([41, 96, 88, 94])
distance = np.array([214, 1789, 1127, 1055])
ans = np.zeros([len(time)])

for race_nr, race_time in enumerate(time):
    for hold_time in range(1, race_time):
        speed = hold_time
        travel_time = time[race_nr] - hold_time
        
        dist = speed * travel_time

        if dist > distance[race_nr]:
            ans[race_nr] += 1
    
print(prod(ans))