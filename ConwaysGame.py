import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# represent 9x9 grid

# 2D numpy array

# OFF = 0; ON = 255;
# prob: OFF = 0.1; ON = 0.9;
# 4*4 = array of 16 values
# reshape converts into a 4x4 2D array
x = np.random.choice([0,255], 4*4, p=[0.1,0.9]).reshape(4,4)

# display matrix as image
# nearest makes cell edges sharper
plt.imshow(x, interpolation='nearest')

# output
plt.show()

