def List_First_Last(List1):
	for i in range(len(List1)):
		if i==0 or i==(len(List1)-1):
			List2.append(List1[i])
	print(List2)
		
List1 = [10,20,40,50,60]
List2 = []
List_First_Last(List1)
