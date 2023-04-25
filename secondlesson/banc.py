print('Вввдеіть суму')
s = float(input())
if s%2==0:
	print(s/2)
else:
	if s%10!=0:
		s=s%10
	else:
		s2=s*10
	if s%100!=0:
		s2=s%100
	else:
		s2=s/100
	if s%1000!=0:
		s2=s%1000
	else:
		s2=s/1000
	print(s)
	print(s2)
    
	
	


