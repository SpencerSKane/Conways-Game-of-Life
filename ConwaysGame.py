import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2,0.8]).reshape(N,N)


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
    """adds a glider with top-left cell at (i, j)"""
    # glider moves steadily across grid
    glider = np.array([[0,0,255],[255,0,255],[0,255,255]])
    # copy pattern array into simulations 2D grid
    grid[i:i+3, j:j+3] = glider
    
def update(frameNum, img, grid, N):
    # copy grid since we reguire 8 neighbors for calculation
    # go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8 neighbor sum using toroidal boundary conditions
            # x and y should "wrap around"
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            # apply Conway's rules
            if grid[i,j] == ON:
                # ON cell turns OFF if it has fewer than 2 neighbors that are ON of if it has more than 3 neighbors that are ON
                if (total < 2) or (total > 3):
                    newGrid[i,j] = OFF
            else:
                if total == 3:
                    # only applies to off cells
                    newGrid[i,j] = ON
                    
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    
def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movFile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', dest='store_true', required=False)
    parser.add_argument('--gosper', dest='store_true', required=False)
    args = parser.parse_args()
    
    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
        
    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)
        
    #declare grid
    grid = np.array([])
    # check if glider demo flag is specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N,N)
        addGlider(1, 1, grid)
    else:
        # populate grid with random on/off
        grid = randomGrid(N)
    
    #set up animation
    fig,ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)
    # number of frames?
    # set the output file
    if args.movfile:
        ani.save(args.mofile, fps=30, extra_args=['-vcodec', 'libx264'])
    # output
    plt.show()
    
# call main
if __name__ == '__main__':
    main()

