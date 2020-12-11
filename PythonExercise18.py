# Given an integer greater than 0, return a list of all possible palindromes of the integer.

x='34322122556656'

l=[]
for j in range(len(x)):
    for i in range(len(x)):
        if x[j]==x[len(x)-1-i]:
            l.append(x[j:len(x)-i])
l1=[]
l2=[]
for t in l:
    if len(t)>1:
        l1.append(t)
l1
for r in l1:
    if r==r[::-1]:
        l2.append(r)

print(list(set(l2)))