# Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the original uncensored string.
# Example
# uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
# uncensor("abcd", "") ➞ "abcd"
# uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

def uncensor(s1,s2): 
    s1_l=[i for i in s1] 
    s2_l=[j for j in s2]
    starindex=[k for k,v in enumerate(s1_l) if v=="*"] 
    
    for a,b in enumerate(starindex):
        s1_l[b]=s2_l[a] 
    
    return ''.join(s1_l)

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))