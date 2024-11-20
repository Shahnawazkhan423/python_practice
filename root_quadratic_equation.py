import math
a1 = int(input("Enter The Value First:"))
b2 = int(input("Enter The Value Second :"))
c3 = int(input("Enter The Value Third :"))
x1 = ((-b2)+(math.sqrt((b2**2)-4*a1*c3)))/(2*a1)
x2 = ((-b2)-(math.sqrt((b2**2)-4*a1*c3)))/(2*a1)
print("Value x1 is:",x1)
print("Value x2 is :",x2)