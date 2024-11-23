def fact(num):
	x = []
	for i in range(2,num):
		if num%i==0:
			x.append(i)
	return x
def prime(y):
	Z = []
	for j in y:
		for k in range(2,j):
			if j%k==0:
				break
		else:
			Z.append(j)	
	return Z
def Ocurrance(num,z):
	global Result
	temp = num
	count = 0
	for m in z:
		while temp>=1 and temp%m==0:
			temp//=m 
			count+=1
		Result[m]=count
		print(Result)
		count=0

num = int(input("Enter The Number:"))
Result = dict()
y = fact(num)
z = prime(y)
print(y)
print(z)
Ocurrance(num,z)
print(Result)