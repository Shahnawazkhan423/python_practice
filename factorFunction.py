def fact(n):
	result=1
	for i in range(1,n+1):
		result*=i
	return result

n= int(input("Enter The Number N:"))
r= int(input("Enter The Number R:"))
x=fact(n)/fact(n-r)
y=fact(n)/(fact(n-r)*fact(r))
print("Permutation Number {} over {} is {}".format(n,r,x))
print("Combination Number {} over {} is {}".format(n,r,y))