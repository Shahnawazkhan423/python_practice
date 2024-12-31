def area(dim1,dim2=None):
	if dim2==None:
		return dim1*dim1
	else:
		return dim1*dim2

x = int(input("Enter The Side:"))
a = int(input("Enter The Length:"))
b = int(input("Enter The Breath:"))
print(area(x))
print(area(a,b))