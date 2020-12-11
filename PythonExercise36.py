# Write a function that returns the closest palindrome number to an integer. If two palindrome numbers tie in absolute distance, return the smaller number.
# Examples
# closest_palindrome(887) ➞ 888
# closest_palindrome(100) ➞ 99
# 99 and 101 are equally distant, so we return the smaller palindrome.
# closest_palindrome(888) ➞ 888
# closest_palindrome(27) ➞ 22

def closest_palindrome(num):

    def addition(plus): 
        global upper
        num_l=[int(i) for i in str(plus)] 
        while num_l!=num_l[::-1]:
            plus+=1
            num_l=[int(i) for i in str(plus)] 
        else:
            upper=plus

    def retraction(minus):
        num_l=[int(i) for i in str(minus)] 
        global lower
        while num_l!=num_l[::-1]:
            minus-=1
            num_l=[int(i) for i in str(minus)] 
        else:
            lower=minus 
    
    addition(num)
    retraction(num)
    if num - lower > upper - num: 
        return upper
    else:
        return lower

print(closest_palindrome(9080))