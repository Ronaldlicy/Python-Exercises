# Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.
# Examples
# next_prime(12) ➞ 13
# next_prime(24) ➞ 29
# next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.

def next_prime(num):
    prime=[num%i==0 for i in range(2,num)]
    if any(prime)==False: 
        return num
    else:
        while any(prime)==True:
            num+=1
            prime=[num%i==0 for i in range(2,num)] 
        else:
            return num 

print(next_prime(24))
