a=[1,2,3,4] ##output=[2,4,6,8]
b=[1,2,3,4]
c=list(zip(a,b))
c=list(map(sum,zip(a,b)))
print(c)
###############OR###############
import numpy as np
a1=np.array(a)
a2=np.array(b)
c=a1+a2
print(c)
