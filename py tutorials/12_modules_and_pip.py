import math
import calendar
import numpy as np
from myutils import vol_cylinder as vc
print(vc(12, 13))

q1 = np.array([
    [200, 220,250],
    [150, 180, 210],
    [300, 330, 360]
])
q2 = np.array([
    [209, 231, 259],
    [155, 192, 222],
    [310, 340, 375]
])

print(q1+q2)
print(q2-q1)

# print(dir(calendar))
# print(calendar.calendar(2026))
# print(dir(math))
# print(dir(dict))

print(format(5, 'b'))