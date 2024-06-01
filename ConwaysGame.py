import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# represent 9x9 grid

# 2D numpy array

# initial condition: Random
#   OFF = 0; ON = 255;
#   prob: OFF = 0.1; ON = 0.9;
#   4*4 = array of 16 values
#   reshape converts into a 4x4 2D array
x = np.random.choice([0,255], 4*4, p=[0.1,0.9]).reshape(4,4)


# TODO: remove next line/ TEMP
N = 4

# initial condition: Particular
def addGlider(i,j,grid):
    # glider moves steadily across grid
    glider = np.array([[0,0,255],[255,0,255],[0,255,255]])
    # copy pattern array into simulations 2D grid
    grid[i:i+3, j:j+3] = glider
# NxN array of 0s
grid = np.zeros(N*N).reshape(N,N)
# initialize grid with glider pattern
addGlider(1,1, grid)

# display matrix as image
# nearest makes cell edges sharper
plt.imshow(x, interpolation='nearest')

# TODO:
# handles wrap around on the right side
# right = grid[i][(j+1)%N]
# handles wrap around on the top side
# right = grid[(i+1)%N][j]

# Conway's Rules
if grid[i,j] == ON:
    # ON cell turns OFF if it has fewer than 2 neighbors that are ON of if it has more than 3 neighbors that are ON
    if (total < 2) or (total > 3):
        newGrid[i,j] = OFF
    else:
        if total == 3:
            # only applies to off cells
            newGrid[i,j] = ON

# output
plt.show()

