# Given a string of decimal digits, output an integer of its binary representation like below:

x="2973"
l_s=[bin(int(i))[2:] for i in x]
l_s 
print(''.join(l_s))