def N_Number_Sum(user):
	temp = 0
	while user!=0:
		digit = user%10
		temp+=digit
		user//=10
	print(temp)
	if temp>9:
		N_Number_Sum(temp)
	else:
		print(temp)
			
user = 123456789112973200	
N_Number_Sum(user)
