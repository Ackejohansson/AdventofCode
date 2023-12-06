import numpy as np

t = 41_968_894
distance = 214_178_911_271_055

hold_time = np.arange(1, t)
speed = hold_time

travel_time = t - hold_time
dist = speed * travel_time

ans = sum(dist > distance)
print(ans)