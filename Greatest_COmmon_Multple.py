User_1 = int(input("Enter The First Number:"))
User_2 = int(input("Enter The Second Number:"))
List_New_1 = []
List_New_2 = []
List_Dup = []
if User_1>1 and User_2>1:
	for i in range(1,User_1+1):
		if User_1%i==0:
			List_New_1.append(i)
	print("List First :",List_New_1)

	for j in range(1,User_2+1):
		if User_2%j==0:
			List_New_2.append(j)
	print("Second List :",List_New_2)	

	for k in List_New_1:
		if  k in List_New_2:
			List_Dup.append(k)
	print("Duplicated Value :",List_Dup)
	print("Grestest Common Multiple Value is :",max(List_Dup))
elif User_1==0 and User_1==0:
	print("Number is: 0")
else:
	print("Negative Not Allowed")





