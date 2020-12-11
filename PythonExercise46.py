# Given an array of strings and an original string, write a function to output an array of boolean values - True if the word can be formed from the original word by swapping two letters only once and False otherwise.
# Examples
# validate_swaps("BACDE", "EBCDA", "BCDEA", "ACBED", "ABCDE") ➞ True, True, False, False
# Swap "A" and "B" from "ABCDE" to get "BACDE". Swap "A" and "E" from "ABCDE" to get "EBCDA". Both "BCDEA" and "ACBED" cannot be formed from "ABCDE" using only a single swap. validate_swaps("32145", "12354", "15342", "12543", "12345") ➞ True, True, True, True
# validate_swaps("9786", "9788", "97865", "7689", "9768") ➞ True, False, False, False

def validate_swaps(arraystrings, originalstring):
    
    validate=[]
    
    for s in arraystrings:

        original=[i for i in originalstring]
        strings=[j for j in s]
        
        if len(strings)!=len(original):
            validate.append(False)
        
        elif sorted(strings)!=sorted(original):
            validate.append(False)
        
        else:
            check=[0 if strings[c]==original[c] else 1 for c in range(len(strings))]

            if sum(check)>2:
                validate.append(False)
            else:
                validate.append(True)
            
    return validate

print(validate_swaps(["9786", "9788", "97865", "7689"], "9768"))