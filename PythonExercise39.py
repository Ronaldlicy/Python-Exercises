# A semiprime is a composite number that is the product of two primes. Apart from these two primes, its only other proper (non-self) divisor is 1.
# The two prime factors of a semiprime can be the same number (e.g. the semiprime 49 is the product of 7x7). A semiprime that has two distinct prime factors is called a squarefree semiprime.
# Create a function that takes a number and returns "Squarefree Semiprime", "Semiprime", or "Neither".
# Examples
# semiprime(49) ➞ "Semiprime"
# semiprime(15) ➞ "Squarefree Semiprime"
# semiprime(97) ➞ "Neither"

def semiprime(num): 
    prime=0
    l=[]
    for i in range(2,num):
        if num % i == 0: 
            l.append(i)
        else: 
            prime+=1
    if num-2==prime: 
        return 'Neither'
    else:
        if len(l)==1:
            return 'Semiprime' 
        elif len(l)==2:
            return 'Squarefree Semiprime' 
        else:
            return 'Neither' 

print(semiprime(97))
