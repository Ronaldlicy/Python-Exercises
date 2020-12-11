# A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.
# 1, 1, 0, 0, 0, 1, 0 Starting from the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.
# So, if we use the example above:
# 1, 1, 0, 0, 0, 1, 0
# You free the prisoner in the 1st cell. 0, 0, 1, 1, 1, 0, 1
# You free the prisoner in the 3rd cell (2nd one locked). 1, 1, 0, 0, 0, 1, 0
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked). 0, 0, 1, 1, 1, 0, 1
# You free the prisoner in the 7th cell - and you are done! Here, we have freed 4 prisoners in total.
# Create a function that, given this unique prison arrangement, returns the number of freed prisoners.
# Examples
# freed_prisoners(1, 1, 0, 0, 0, 1, 0) ➞ 4
# freed_prisoners(1, 1, 1) ➞ 1
# freed_prisoners(0, 0, 0) ➞ 0
# freed_prisoners(0, 1, 1, 1) ➞ 0

def freed_prisoners(cell):
    
    if cell[0]==0:
        return 0
    
    else:
        count=0
        for i in range(len(cell)):
            if cell[i]==1:
                cell=[1 if j==0 else 0 for j in cell]
                count+=1
        return count
        
print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))