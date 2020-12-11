# Given a string, create a function that splits the string into pairs of two characters. Put the pairs inside a list then return the list. If a character is missing in a pair, use the character '?' to replace the missing character.

s="abcdefghi"
s_l=[i for i in s]
if len(s_l)%2!=0:
    s_l.extend('?')
else:
    pass
outputlist=[s_l[j]+s_l[j+1] for j in range(len(s_l)) if j%2==0]

print(outputlist)