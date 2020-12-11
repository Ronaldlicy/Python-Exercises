# Create a function that takes a list and returns a new list containing only prime numbers.
# Examples
# filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]
# filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]
# filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]

def filter_primes(l1):
    l2=[]
    for i in range(len(l1)): 
        if l1[i]==1:
            l2.append(i) 
        else:
            for j in range(2,l1[i]): 
                if l1[i]%j==0:
                    l2.append(i) 
    popout=list(set(l2))
    counter=0
    for p in popout:
        l1.pop(p-counter)
        counter+=1 
    return l1

print(filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]))