import math
a_user = int(input("Enter The First  Value:"))
b_user = int(input("Enter The Second Value:"))
c_user = int(input("Enter The Third  Value:"))
temp = (b_user**2)-(4*a_user*c_user)
print("The Discriminant is:",temp)
if temp>0:	
	x = ((-b_user)+math.sqrt(temp))/(2*a_user)
	y = ((-b_user)-math.sqrt(temp))/(2*a_user)
	print("Discriminant value is positive, the quadratic equation has two real and distinct solutions: x = {} ,y = {}".format(int(x),int(y)))
elif temp==0:
	x = ((-b_user)+math.sqrt(temp))/(2*a_user)
	y = ((-b_user)-math.sqrt(temp))/(2*a_user)
	print("Discriminant value is zero, the quadratic equation has only one solution or two real and equal solutions: x = {} ,y = {}".format(int(x),int(y)))
elif temp<0:
	print("The square root of a negative number is not a real number; instead, it results in an imaginary number.")
	print("Therefore, the quadratic equation has no real solutions, but it has two complex (imaginary) solutions.")
else:
	print("Inalid Syntax")