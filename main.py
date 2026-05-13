import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# generates a matrix of zeros
grid = np.zeros((50,50), dtype=int)

# vertical central column
grid[24, 25] = 1
grid[25, 25] = 1
grid[26, 25] = 1

# gets the neighbours of the grid spots
neighbour = (
    np.roll(grid, 1, axis=0) + # north
    np.roll(grid, -1, axis=0) + # south
    np.roll(grid, 1, axis=1) + # west
    np.roll(grid, -1, axis=1) + # east
    np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
    np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
    np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
    np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
)
# this variable allows for simultaneous application of the rules
new_grid = np.zeros_like(grid)

# rule: live cell with 2 or 3 neighbours survives
new_grid[(grid == 1) & ((neighbour == 2) | (neighbour == 3))] = 1
# rule: dead cell with exactly 2 neighbouts becomes alive
new_grid[(grid == 0) & (neighbour == 3)] = 1

grid = new_grid

fig, ax = plt.subplots()
ax.axis('off')
im = ax.imshow(grid, cmap='PuBu', interpolation='nearest')

# puts the matrix on a graph and displays it
plt.imshow(grid, cmap="binary", interpolation="nearest")
plt.axis("off")
plt.show()