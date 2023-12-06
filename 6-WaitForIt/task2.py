import numpy as np
from math import prod

time = 41_968_894
distance = 214_178_911_271_055
ans = 0

for hold_time in range(1, time):
    speed = hold_time
    travel_time = time - hold_time
    
    dist = speed * travel_time

    if dist > distance:
        ans += 1
    
print(ans)