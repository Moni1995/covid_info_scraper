import numpy as np
from math import sqrt
from sympy import *
o1 = np.array([-3.49650,8.18345,-2.06959])
o2 = np.array([-1.17552,6.99500,-4.02865])
vector_a = o1-o2

mid_o1_o2 = vector_a/2
o_Th = np.linalg.norm(o1-o2)*(0.5)
print(vector_a)
print(mid_o1_o2)
print(o_Th)

radius = sqrt(2.3**2 - o_Th**2)
print(radius)

# o1o2 * (plane - mid_o1_o2) = 0
# [-2.32098  1.18845  1.95906] * ([x,y,z] - radius) = 01
#qua = vector_a[0] * (x - mid_o1_o2[0]) + vector_a[1] * (y - mid_o1_o2[1]) + vector_a[2] * (z - mid_o1_o2[2])
-2.3209*(x-(-1.16049))+   1.18845*(y-(0.594225)) +  1.95906*(z-(0.97953)) = 0
#qua1 = simplify(qua)
#print(qua)