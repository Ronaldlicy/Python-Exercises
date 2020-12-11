# Given an input integer x, return a list of integers in which the sum is equal to x. The integers inside the list must consist of values that are a power of 3. For example:
# 1 is a possible number of the list because of 3^0 => 1
# 3 is also a possible number of the list because 3^1 => 3
# and so on.

import math
x=25
l1=[] 
y=math.floor(math.log(x,3))
for i in range(y+1)[::-1]:
    while x>=3**i:
        x=x-3**i
        l1.append(3**i)

print(l1)