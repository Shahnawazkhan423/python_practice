import timeit
def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)
x = int(input("Enter The Factorial Number:"))
y= fact(x)
print(timeit.timeit(y))