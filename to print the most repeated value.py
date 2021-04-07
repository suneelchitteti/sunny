a=[1,2,3,4,2,3,5,3,6,3,7]
d={}
c=[]
for i in a:
    d[i]=d.get(i,0)+1
print(d)
for k in d.items():
    print(k)
#print(c)
#print(max(c))
    #print(a1)
   # print(k,"is occured in",v,"times")
