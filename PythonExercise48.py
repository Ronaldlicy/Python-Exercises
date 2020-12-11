# Suppose any nxm matrix of 0s and 1s can be transformed into a second matrix, where each number in position (i, j) in the new matrix is the sum of 1s in row i and column j in the original matrix, excluding itself (if it is a 1).
# [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
# 1, 5, 2, 4, 1, 2, 4, 1, 3, 2, 2, 4, 1, 1, 2, 3, 2, 2, 2, 3, 2, 2, 1, 3, 2
# The 1 on the upper left corner has 1 other 1 in the same row as itself (excluding itself). The 0 to the right of the 1 has 2 1's on the same row as itself, and 3 1's in the same column, etc. Create a function that transforms the first matrix into its second matrix equivalent.
# Examples
# transform_matrix([ 1, 0, 0, 0, 1, 0, 0, 0, 1 ]) ➞ [ 0, 2, 2, 2, 0, 2, 2, 2, 0 ]
# transform_matrix([ 1, 1, 1, 0, 0, 1, 0, 0, 1 ]) ➞ [ 2, 2, 4, 2, 2, 2, 2, 2, 2 ]
# transform_matrix([ 1, 1, 1, 0, 1, 1, 0, 0, 1 ]) ➞ [ 2, 3, 4, 3, 2, 3, 2, 3, 2 ]

def transform_matrix(original_list):
    big_list=original_list.copy()
    big_sub_list=[]
    for j, l in enumerate(original_list):
        big_list.pop(j)
        sub_list=[]
        for i in range(len(l)):
            vertical=[l[i] for l in big_list]
            x=l.pop(i)
            sub_list.append(sum(l) + sum(vertical))
            l.insert(i,x)
        big_sub_list.append(sub_list)
        big_list=original_list.copy()
    return big_sub_list

print(transform_matrix([ [1, 0, 0], [0, 1, 0], [0, 0, 1] ]))
print(transform_matrix([ [1, 1, 1], [0, 0, 1], [0, 0, 1] ]))
print(transform_matrix([ [1, 1, 1], [0, 1, 1], [0, 0, 1] ]))