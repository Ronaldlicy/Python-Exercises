# Given a string, count all the lowercase letters. Return a dictionary with the keys as the lowercase letters and the values as the letters' counts respectively. The keys should be sorted in alphabetical order.

s= "apple" 
l=[]
dict1={}
for i in s:
    l.append(i)
l.sort()
for j in l:
    dict1[j]= l.count(j)

print(dict1)