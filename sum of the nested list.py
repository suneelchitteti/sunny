a=[1,2,3,4,[1,2,3,4],(1,2,3,4),{1,2,3,4},1,2,3,4]
print('this is supports the all int and list and tuple and set')
c=[]
b=0
for i in a:
    if type(i)==list:
        for j in i:
            b+=j
            c.append(j)
    elif type(i)==tuple:
        for j in i:
            b+=j
            c.append(j)
    elif type(i)==set:
        for j in i:
            b+=j
            c.append(j)
    else:
        b+=i
        c.append(i)
        
        

print(b)
print(sum(c))

print('this is support the only integer values')

a=[[1,2,3,4],(1,2,3,4),{1,2,3,4}]
d=0
for i in a:
    for j in i:
        d+=j
print(d)



#
##
##    if type(int)==list:
##        b.append(i)
##    elif type(int)==tuple:
##        b.append(i)
##    else:
##        b.append(i)
##
##
##print(b)
##c=sum(b)
##print(c)










##
##b=0
##for i in a:
##    if type(i)==list:
##        for j in i:
##            b+=j
##    else:
##        b=b+i
##print(b)
