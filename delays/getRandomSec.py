import random as r
import numpy as np

center_min = 30.0
std_min    = 10.0
val = np.random.normal(loc=center_min, scale=std_min)

print(val)


if val < 0.0:
  val = 0.0

if val > 60.0:
  val = 60.0

ret_double = val * 60.0

ret = int(ret_double)

#print(ret)
