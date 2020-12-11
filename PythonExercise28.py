# A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function that returns True if a string is an almost-palindrome and False otherwise.
# Examples
# almost_palindrome("abcdcbg") ➞ True
#Transformed to "abcdcba" by changing "g" to "a".
# almost_palindrome("abccia") ➞ True
#Transformed to "abccba" by changing "b" to "a".
# almost_palindrome("abcdaaa") ➞ False
#Can't be transformed to a palindrome in exactly 1 turn.
# almost_palindrome("1234312") ➞ False

def almost_palindrome(s1):
    counter=0
    if len(s1)%2==0:
        for k,v in list(zip(s1[0:int(len(s1)/2)],s1[int(len(s1)/2):len(s1)][::-1])):
            if k!=v:
                counter+=1
    else:
        for k,v in list(zip(s1[0:int(len(s1)/2)],s1[int(len(s1)/2)+1:len(s1)][::-1])):
            if k!=v: 
                counter+=1
    return counter<2
    
print(almost_palindrome("1234312"))