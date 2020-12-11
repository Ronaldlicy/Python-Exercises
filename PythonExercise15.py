# Given two lists of any data type, return a list that combines the two lists by alternating the elements passed. The input lists can be of different lengths.

l1=[1, 2, 3, 4, 5]
l2=['a', 'b', 'c']

counter=0

for i in range(len(l1)):
    l2.insert(counter,l1[i])
    counter+=2

print(l2)
