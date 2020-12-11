# Given an integer n, find all the integers that is the multiple of 3 from 0 to n. Return the sum of all these integers.

x=31
a=x//3
counter=1
l1=[]

for i in range(a):
    l1.append(3*counter)
    counter+=1

print(l1)
