c=4500
money=[5,10,20,50,100,200,500,1000]
count=[]
for i in range(0,len(money)):
    if c%money[i]==0:
        count.append(c//money[i])
    else:continue
min=count[0]
ind=0
for i in range(0, len(count)):
    if min>count[i]:
        min=count[i]
        ind=i+1
m=money[ind]
print(count)
print(money)
print("банкомат видав "+str(m)+" купюр номіналом "+str(min))


 
