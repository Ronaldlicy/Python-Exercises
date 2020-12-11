# Given any number, we can create a new number by adding the sums of squares of digits of that number. For example, given 203, our new number is 4 + 0 + 9 = 13. If we repeat this process, we get a sequence of numbers:
# 203 -> 13 -> 10 -> 1 -> 1 Sometimes, like with 203, the sequence reaches (and stays at) 1. Numbers like this are called happy.
# Not all numbers are happy. If we started with 11, the sequence would be:
# 11 -> 2 -> 4 -> 16 -> ... This sequence will never reach 1, and so the number 11 is called unhappy.
# Given a positive whole number, you have to determine whether that number is happy or unhappy.
# Examples
# happy(203) ➞ True
# happy(11) ➞ False
# happy(107) ➞ False

def happy(num):
    num_l=[int(i) for i in str(num)]
    while len(num_l)>1:
        for j in range(len(num_l)):
            num_l[j]=num_l[j]**2
        num_l=[int(i) for i in str(sum(num_l))]
    return num_l[0]==1 
    
print(happy(302))
