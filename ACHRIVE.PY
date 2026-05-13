def animate(i):
    t= 0.1*i

fig, ax = plt.subplots()
ax.axis('off')
im = ax.imshow(grid, cmap='PuBu', interpolation='nearest')

counter = 0
for x in range(50):
    counter += 1
    for y in range(50):
        counter += 1
        if counter%2 == 1:
            grid[x,y] = 0.15
