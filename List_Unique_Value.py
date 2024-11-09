user = int(input("How Many Insert Value: "))
user_List = []
Empty_List = []
for i in range(1,user+1):
	Value = int(input("Enter The Value: "))
	user_List.append(Value)
print("This is a List:",user_List)
for j in user_List:
	if j not in Empty_List:
		Empty_List.append(j)
		print("Unique Value in List: ",Empty_List)
		
#***************************Function*********************************
"""def Unique_List(user):
	user_List = []
	Empty_List = []
	for i in range(1,user+1):
		Value = int(input("Enter The Value: "))
		user_List.append(Value)
	print("This is a List:",user_List)
	for j in user_List:
		if j not in Empty_List:
			Empty_List.append(j)
			print("Unique Value in List: ",Empty_List)
		else:
			Empty_List.remove(j)

user = int(input("How Many Insert Value: "))
Unique_List(user)
"""