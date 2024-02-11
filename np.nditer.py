# Import numpy as np
import numpy as np


# For loop over np_height
for val in np_height:
    print(str(val) + " inches")


# For loop over np_baseball - array od arrays
for val in np.nditer(np_baseball):
    print(val)