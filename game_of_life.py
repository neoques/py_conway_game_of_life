import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt

# Init
board = np.array([
        [ 1, 1, 1],
        [ 0, 0, 1],
        [ 0, 1, 0]], 
    dtype=int)

board = np.pad(board, 4)

# Rules
def rules(local_grid):
    live_neighbors = np.sum(local_grid)
    return live_neighbors == 3 or (live_neighbors - local_grid[4]) == 3

# Animate
plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(board, cmap='binary')
plt.show()

while True:
    img.set_data(board := scipy.ndimage.generic_filter(board, rules, (3,3), mode = 'wrap'))
    plt.draw()
    plt.pause(0.1)
    if not plt.fignum_exists(fig.number):
        break

plt.ioff()
plt.close()