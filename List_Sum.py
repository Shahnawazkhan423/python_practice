def Min_Value(List1):
	for i in range(len(List1)):
		temp=0
		while List1[i]!=0:
			digit = List1[i]%10
			List1[i]//=10
			temp+=digit
		List2.append(temp)
		maximum = max(List2)
		minimum = min(List2)
	print("Sum is all Number:",List2)	
	print("Minimum Value",minimum)
	print("Maximum Value",maximum)

List1 = [10,99,11]
List2=[]
Min_Value(List1)


	