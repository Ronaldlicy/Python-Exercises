# Given a string, return the character with the most value. The value of a character is the difference between the index of its first occurrence and the index of its last occurrence. If there is a tie, return the character that goes first alphabetically.

s='abcdbcd'
s_l=[i for i in s]
dict_s={j:(len(s_l)-1-s_l[::-1].index(j))-(s_l.index(j)) for j in set(s_l)}
l1=[k for k in dict_s if dict_s.get(k)==max(dict_s.values())]
l1.sort()
print(l1[0])