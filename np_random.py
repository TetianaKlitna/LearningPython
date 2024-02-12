# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step += step
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(str(dice) + " " + str(step))