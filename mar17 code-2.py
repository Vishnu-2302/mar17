h=input()
l=0
u=0
d=0
s=0
for i in h:
	if(i.islower()):
		l=l+1
	elif(i.isupper()):
		u=u+1
	elif(i.isdigit()):
		d=d+1
	else:
		s=s+1
if l>=1:
	if u>=1:
		if d>=1:
			if s>=1:
				print('password is valid')
			else:
				print('invalid must include a Symbol')
		else:
			print('invalid must include a Digit')
	else:
		print('invalid must include a Upper case')
else:
	print('invalid must include a Lower case')