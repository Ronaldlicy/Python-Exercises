# Write a function that replaces each integer with the next largest in the list.
# Examples
# replace_next_largest(5, 7, 3, 2, 8) ➞ 7, 8, 5, 3, -1
# replace_next_largest(2, 3, 4, 5) ➞ 3, 4, 5, -1
# replace_next_largest(1, 0, -1, 8, -72) ➞ 8, 1, 0, -1, -1

def replace_next_largest(l1):
    
    l1_sorted=sorted(l1)

    for i,j in enumerate(l1):
        if j==max(l1):
            l1[i]=-1
        else:
            l1[i] = l1_sorted[l1_sorted.index(j)+1]
    return l1

print(replace_next_largest([1, 0, -1, 8, -72]))