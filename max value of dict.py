a={'a':1,'b':2,'x':5,'d':3,'e':4}
d=sorted(a.values())
#print(d)
d1=d[-1]
#print(d1)
'''
for i in a.keys():
    #print(i)
    #print(a[i])
    if a[i]==d1:
        print(i)
'''
for i in a.items():
    #print(i)
    if i[1]==d1:
        print(i[0],':',d1)
    


x=sorted(a.items())
y=x[-1]
print(x[0],':',




'''
#output----max valu...5

##
##b=a.items()
##print(b)
##c=sorted(a.values())
##print(c)
##print(max(c))
##
##
##d=sorted(a.keys())
##print(d)
##print(d[2])
##
##
e=sorted(a.items())
print(e)


f=dict(e)
print(f)
print(len(f))
h=e[-1]


g=dict(h)
print(g)
'''
