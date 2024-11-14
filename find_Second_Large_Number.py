def Second_Large_Num(user):
	List1 =[]
	Empty_List=[]
	for i in range(user):
		user_Sec = int(input("Enter The Value:"))
		List1.append(user_Sec)
	print(f"Unorder List: {List1}")
	List1.sort()
	print(f"Order List:{List1}")
	for j in List1:
		if j not in Empty_List:
			Empty_List.append(j)

	element = Empty_List[-2]
	print("Second Largest Value:",element)		


user = int(input("How Many Value Enter You : "))
Second_Large_Num(user)