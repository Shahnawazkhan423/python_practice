"""user = int(input("Enter Value:"))
user_sec = int(input("Enter Value:"))
temp=user
x = []
for i in range(2,user):
	if temp%i==0 and temp>=1:
		temp//=i
		x.append(i)
print(x)
string =""
for j in x:
	if string=="":
		string=j
	else:
		string="{}*{}".format(string,j)
print("{} = {}".format(user,string))
z = []
for l in x:
	if l in y:
		z.append(l)
print(z)
"""
#*************************Function***************************/
def factorize(number):
	factors = []
	temp = number
	i=2
	while temp!=1:
		if temp%i==0:
			temp//=i
			factors.append(i)
		else:
			i+=1
	return factors
def fomate_factor(factors):
	string =""
	for j in factors:
		if string=="":
			string=j
		else:
			string="{}*{}".format(string,j)
	return string

user = int(input("Enter The First Value:"))
user_sec = int(input("Enter The Second Value:"))

x =factorize(user)
y =factorize(user_sec)

print(x)
print("{} = {}".format(user,fomate_factor(x)))

print(y)
print("{} = {}".format(user_sec,fomate_factor(y)))

z = []
for j in x:
	if j in y:
		z.append(j)
if len(z)==0:
	print("Not Match Value")		
else:	
	print("Common Value :",z)
	print("Greatest Value :",z[-1])
	


