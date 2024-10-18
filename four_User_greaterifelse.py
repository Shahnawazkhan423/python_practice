a = int(input("Enter The Value a:-"))
b = int(input("Enter The Value b:-"))
c = int(input("Enter The Value c:-"))
d = int(input("Enter The Value d:-"))
if a<=b and  a<=c and a<=d:
	print("a is smallest")
elif b<=a and b<=c and b<=d:
	print("b is smallest")
elif c<=a and c<=b and c<=d:
	print("c is smallest")
else:
	print("d is smallest")
