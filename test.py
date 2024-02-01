# """A"""
# import sys
# input = sys.stdin.readline().split()
# a, b = list(map(int, input))
# def get_age(a, b):
#     if a == 0 and b == 0:
#         return "Not a moose"
#     if a == b:
#         return f"Even {a+b}"
#     return f"Odd {max(a, b) * 2}"

# print(get_age(a, b))

# """B"""
# import sys
# import numpy as np

# input = sys.stdin.readline().split()
# r, c = list(map(int, input))

# total_area = np.pi * r**2
# cheese_area = np.pi * (r-c)**2

# print(cheese_area/total_area * 100)



# C
import numpy as np
grid_size, nr_boats = map(int, input().split())

grid = np.array([list(input()) for _ in range(grid_size)])
boat_sizes = [int(input()) for _ in range(nr_boats)]

print("Grid Size:", grid_size)
print("Number of Boats:", nr_boats)
print("Grid:")
for row in grid:
    print(row)
print("Boat Sizes:", boat_sizes)
print(grid[0])
print(grid[1][1])


def is_boat_placed(grid, boat_sizes):
    """ Checks if boat is placed """
    pass
    rows, cols = np.where(grid == 'O')
    boat_coords = list(zip(rows, cols))

    # If all columns are O then  -> ship found
    # If any edge and then everything up to X a ship is found
    # If everything between 2 X is O -> found

    # If nr O in a row matches longest ship -> found
    # If ship found: Set to X



# for boat in boat_sizes:
#     is_boat_placed()
#     row1 = grid[0]



