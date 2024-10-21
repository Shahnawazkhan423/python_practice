a=int(input("Enter the Value a:-"))
b=int(input("Enter the Value b:-"))
c=int(input("Enter the Value c:-"))
if a>b and a>c:
	print("a is greater")
elif b>a and a>c:
	print("b is greater")
else:
	print("c is greater")