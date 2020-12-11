# Given a list of integers, create a function that finds the odd one out in the list.
 
def theoddone(l):
    l_trim=list(set(l))
    dict1={}
    for i in range(len(l_trim)):
        dict1[l_trim[i]]=l.count(l_trim[i])
    for key, value in dict1.items():
        if value == 1:
            return key

print(theoddone([1,1,1,1,1,1,2,1]))
