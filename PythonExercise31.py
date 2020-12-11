# Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.
# Examples
# censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
# censor_string("The cow jumped over the moon.", ["cow", "over"], "*") ➞ "The *** jumped **** the moon."
# censor_string("Why did the chicken cross the road?", ["did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

def censor_string(s1,l1,char): 
    s1_l=[i for i in s1] 
    s1_l2=[]
    temp=''
    for j in s1_l:
        if j.isalpha()==True: 
            temp+=j
        else: 
            s1_l2.append(temp) 
            s1_l2.append(j) 
            temp=''
    for i in range(len(s1_l2)): 
        if s1_l2[i] in l1:
            s1_l2[i]=char*len(s1_l2[i]) 
    return ''.join(s1_l2)

print(censor_string("Why did the chicken cross the road?", ["did", "chicken", "road"], "*"))