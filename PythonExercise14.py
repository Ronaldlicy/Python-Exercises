# Given a list of integers, split the list into two, put the arrays on top of each other, then add them together. Return the finished list.

import numpy as np

l1=[1, 2, 3, 4, 5, 6, 7,8]
l2=[]
for i in range(0,int(len(l1)/2)):
    x=l1.pop(0)
    l2.append(x)
a=np.array(l2)
b=np.array(l1)
if len(l2)<len(l1):
    a=np.concatenate([a, np.zeros(1)])
else: 
    pass
print(a+b)