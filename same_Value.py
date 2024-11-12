def Same(user):
	Emp= ""
	Sec_Emp = ""
	for i in user:
		if i not in Emp:
			Count =user.count(i)
			Emp+=i
			Sec_Emp+= f"{i}{Count}-"
	return Sec_Emp
			
user =input("Enter The Value:")
result = Same(user)
print(result)

