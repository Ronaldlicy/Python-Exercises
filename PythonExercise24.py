# Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

import random
x=random.randrange(10000, 99999)
print(x)
l_max=sorted([i for i in str(x)], reverse=True)
l_min=sorted([j for j in str(x)])
if l_min[0]=='0':
    l_min[0],l_min[l_min.count('0')]=l_min[l_min.count('0')],l_min[0]

print(''.join(l_max))
print(''.join(l_min))

print('The differenc:',int(''.join(l_max))-int(''.join(l_min)))

