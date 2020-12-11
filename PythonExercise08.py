# Given two integer inputs n and d, create a function that squares all numbers from 1 to n, then returns the count of all instances of d from the square results.

n=5 
d=1
l=[]
counter=0
for i in range(n):
    a=(i+1)**2
    l.append(a) 
print(l)

for b in l:
    if len(str(b))>1:
        c=[i for i in str(b)]
        for e in c:
            if e==str(d):
                counter+=1
    elif len(str(b))==1:
        if str(b)==str(d):
            counter+=1
print(counter)