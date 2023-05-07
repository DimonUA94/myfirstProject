import sys
import sys
f=open("print_2.py", "r")	
f2=open("print_4.py", "w")	
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
	f2.write(lines[id])
	count-=1
f.close()
f2.close()	
