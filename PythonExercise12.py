# Given a list of 5 floats, return a tuple of the average of the middle 3 floats and the lowest float of that list.

f1=[6.4, 11.4, 7.6, 10.5, 8.1]
shifter=0
if len(f1)>5:
    shifter+=int((len(f1)-5)/2)
    x=round((f1[1+shifter]+f1[2+shifter]+f1[3+shifter])/3,2)
else:
    x=round((f1[1+shifter]+f1[2+shifter]+f1[3+shifter])/3,2)

print(x,min(f1))