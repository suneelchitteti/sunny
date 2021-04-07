import copy 
  
# initializing list 1  
li1 = [1, 2, [3,5], 4] 
  
  
# using copy for shallow copy   
li2 = copy.copy(li1)
li21=li2[2][0]=5
print(li21)
  
# using deepcopy for deepcopy   
li3 = copy.deepcopy(li1)  
print(li3)
