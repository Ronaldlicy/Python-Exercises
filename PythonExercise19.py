# Given a string of names with a certain pattern, return a formatted string with a certain pattern. 

z = "Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison"
def transformstring(x):
    a = x.split(';')
    l1=[]
    dict1={}
    for i in a:
        dict1[i.split(':')[0]]=i.split(':')[1] 
    for j in range(len(dict1.values())):
        b=f'({list(dict1.values())[j]},{list(dict1.keys())[j]})'
        l1.append(b)
    return (''.join(l1))

print(transformstring(z))