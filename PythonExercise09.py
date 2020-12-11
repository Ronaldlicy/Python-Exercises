# Given a string, add or subtract numbers and return the answer.

s1='2minus6plus4plus7' 
l_plus=s1.split('plus')
l_sum=[]
l_subtract=[]
for i in l_plus:
    if i.isdigit()==True:
        l_sum.append(int(i))
    else:
        l_minus=i.split('minus')
for j in l_minus:
    if j.isdigit()==True:
        l_subtract.append(-int(j))
l_subtract[0]=-l_subtract[0]

print(sum(l_sum)+sum(l_subtract))