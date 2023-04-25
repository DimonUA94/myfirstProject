import sys
f=open("print_2.py", "r")	
sum=0
for i in range(1,13):
  sum+=1
for line  in f:
	print(line)
f.close()
