import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# generates a matrix of zeros
grid = np.zeros((50,50), dtype=int)

# vertical central column
grid[25, 24] = 1
grid[25, 25] = 1
grid[25, 26] = 1
grid[24, 26] = 1
grid[23, 25] = 1


grid[9, 10] = 1
grid[9, 11] = 1
grid[10, 9] = 1
grid[10, 10] = 1
grid[11, 10] = 1


grid[19, 20] = 1
grid[19, 21] = 1
grid[20, 19] = 1
grid[20, 20] = 1
grid[21, 20] = 1


def update(frame):
    global grid

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
    survive = (grid == 1) & ((neighbour == 2) | (neighbour == 3))
    # rule: dead cell with exactly 2 neighbouts becomes alive
    born = (grid == 0) & (neighbour == 3)

    new_grid[survive] = 1
    new_grid[born] = 1

    grid = new_grid

    im.set_data(grid)
    return (im,)
    

fig, ax = plt.subplots()
ax.axis('off')
im = ax.imshow(grid, cmap='PuBu', interpolation='nearest')

ani = animation.FuncAnimation(fig,
                              update,
                              frames=200,
                              interval=25,
                              blit=True)

# puts the matrix on a graph and displays it
plt.imshow(grid, cmap="PuBu", interpolation="nearest")
plt.axis("off")
plt.show()