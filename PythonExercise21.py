# Given a list of mixed integers of different representations, add up the non-string integers and subtract this from the total of string integers.

x=[1, '2', 3, '4', 5]
l_s=[]
l_i=[]
for i in x:
    if type(i)==str:
        l_s.append(int(i))
    else:
        l_i.append(i)

print(sum(l_s)-sum(l_i))