s=input("Enter a string:")
m=len(s)
c=0
if(s!=s[::-1]):
	m1=int(m/2)
	k=0
	k1=len(s)-1
	for i in range(m1):
			if(s[k]==s[k1]):
				   k+=1
				   k1-=1
				   continue
			else:
				 c+=1
				 k+=1
				 k1-=1
	print(c)
else:
	print(c)

				


	

