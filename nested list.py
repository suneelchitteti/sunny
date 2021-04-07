a=[[1,2,3,4],[1,2,3,4]] #output=[2,4,6,8]
b=len(a[0])
c=[]
for i in range(b):
    result=a[0][i]+a[1][i]
    c.append(result)
print(c)
