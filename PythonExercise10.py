# Given an integer, create a function that finds and returns the length of the longest binary gap of the binary representation of that integer. A binary gap is the sequence of consecutive zeros in between ones in a binary representation. Reference for binary representation can be found here: https://www.rapidtables.com/convert/number/decimal-to-binary.html

x=527
x_bin=bin(x)[2:]
l_zero=[i for i in x_bin.split('1')if i.isdigit()==True]
if not l_zero:
    print (0)
else:
    ans=max([len(j) for j in l_zero])
    print(ans)