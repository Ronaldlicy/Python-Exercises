# Create a function that removes all capital letters and punctuation in a string. Return the clean string.

import string
def clean_string(s):
    new_s = s
    for i in s:
        if i.isupper() or i in string.punctuation:
            new_s = new_s.replace(i,'')
    return new_s

print(clean_string('HellO...wOrld'))