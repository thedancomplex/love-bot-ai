import random as r
import numpy as np

max_min    = 30.0
center_min = 13.0
std_min    = 6.0
val = np.random.normal(loc=center_min, scale=std_min)

# Print number of minutes
#print(val)

if val < 0.0:
  val = -val

if val < 0.0:
  val = 0.0

if val > max_min:
  val = max_min

ret_double = val * 60.0

ret = int(ret_double)

# Print number of seconds
print(ret)
