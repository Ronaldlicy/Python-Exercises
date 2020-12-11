# Create a function that given an n positive integer, it sums all the cubed values from 1 to n. Return the sum.


def sum_cubes(n):
    list1= [i**3 for i in range(1,n+1)] 
    return sum(list1)

print(sum_cubes(4))