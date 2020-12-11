# Given a list of 11 integers, return a string in the form of a Hong Kong phone number in this format: +852 xxxx xxxx

# Only the numbers 2, 3, 5, 6, 7, and 9 can be added after the extension 852.

eleven=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

y=[i for i in eleven if i not in [8,5,2]]
z=[]
while y[0] not in [2,3,5,6,7,9]:
    for j in range(len(y)):
        y[0],y[len(y)-1-j]=y[len(y)-1-j],y[0]
for k in y:
    z.append(str(k))
z.insert(0,'')
z.insert(5,'')
a=''.join(z)
b=a
b
print(f'+852 {b[0:4]} {b[4:9]}')


