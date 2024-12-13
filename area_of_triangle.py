import math
a_user = int(input("Enter The First  Value (Side 1) :"))
b_user = int(input("Enter The Second Value (Side 2) :"))
c_user = int(input("Enter The Third  Value (Side 3) :"))
base = int(input("Enter The Base :"))
semi = (a_user+b_user+c_user)/2
area = math.sqrt(semi*(semi - a_user)*(semi - b_user)*(semi - c_user))
height = (2*area)/base
A = 1/2*(base*height)
print(area)
print(height)
print(A)