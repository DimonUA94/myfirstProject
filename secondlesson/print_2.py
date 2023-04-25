import sys
f=open("print_2.py", "r")	
sum=0
for i in range(1,13):
  sum+=1
lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
print(len(lines))
count=len(lines)
for id, item in enumerate(lines):
	id=count-1
	print(lines[id])
	count-=1
f.close()
