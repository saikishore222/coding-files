import math
N=int(input("Enter a number:"))
if(N>=0 and N<=1024):
		m=pow(2,N)
		m1=str(m)
		m2=len(m1)-1
		for i in range(m2,-1,-1):
				if(m1[i]==0):
					s.replace(m1[i],'')
				else:
					break
		m3=str(m1)
		print(m3)
else:
	print("input is out of range")
