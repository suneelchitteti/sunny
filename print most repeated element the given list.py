import statistics
from  statistics import mode
a=[1,2,3,2,3,4,5,3,4,5,6,3,3]
d=mode(a)
print("the most repeated value in given python list is:",d)
###########another way###########
b=max(set(a),key=a.count)
print(b)
