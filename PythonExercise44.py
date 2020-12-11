# In numbers theory, a positive composite integer is a Smith number if its digital root is equal to the digital root of the sum of its prime factors, with factors being counted by multiplicity. Trivially, every prime is also a Smith number, having just one prime factor that is equal to itself. If two Smith numbers are consecutive in the integer series, then they are Smith brothers. Any other number will not be a Smith.
# Given a positive integer number, implement a function that returns:
# "Youngest Smith" if the given number is the lower element of a couple of Smith brothers. "Oldest Smith" if the given number is the higher element of a couple of Smith brothers. "Single Smith" if the given number is a Smith number without another Smith number adjacent, lower or higher. "Trivial Smith" if the given number is a prime. "Not a Smith" if the given number is not a Smith number. Examples
# smith_type(22) ➞ "Single Smith"
# Digital root of 22 = 2 + 2 = 4 Sum of prime factors of 22 = 2 + 11 = 13 Digital root of 13 = 1 + 3 = 4 Is a Smith number without a brother smith_type(7) ➞ "Trivial Smith"
# The given number is a prime smith_type(728) ➞ "Youngest Smith"
# Digital root of 728 = 7 + 2 + 8 = 17 = 1 + 7 = 8 Sum of prime factors of 728 = 2 + 2 + 2 + 7 + 13 = 26 Digital root of 26 = 2 + 6 = 8 The number 729 is a Smith number, so 728 is the youngest brother smith_type(6) ➞ "Not a Smith"
# Digital root of 6 = 6 Sum of prime factors of 6 = 2 + 3 = 5 Digital root of 5 = 5

def smith_type(num):

    def digitalroot(x):
        l_x=[int(i) for i in str(x)]
        while len(l_x)>2:
            l_x2=[int(i) for i in str(sum(l_x))]
            return sum(l_x2)
        else:
            return sum(l_x)

    def checkprime(y):
        prime=[y%i==0 for i in range(2,y)]
        return any(prime)==False

    def primfactor(z):
        l=[]
        l2=[]
        while z%2==0:
            z/=2
            l.append(2)
        else:
            if checkprime(int(z))==True:
                l2.append(int(z))
            else:
                for i in range(2,int(z)):
                    if z%i==0:
                        l2.append(i)
        return l+([i for i in l2 if checkprime(i)==True])

    if num==primfactor(num)[0]:
        return "Trivial Smith"

    elif (digitalroot(num)==digitalroot(sum(primfactor(num))))==True:
        if (digitalroot(num+1)==digitalroot(sum(primfactor(num+1))))==True:
            return "Youngest Smith"
        elif (digitalroot(num-1)==digitalroot(sum(primfactor(num-1))))==True:
            return "Oldest Smith"
        else:
            return "Single Smith"

    else:
        return "Not a Smith"

print(smith_type(6))