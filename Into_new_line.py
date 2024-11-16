def Intro(user_Sub,user_Address,user_Roll,user_Name):
	print()
	print(f"Hii My Name is {user_Name},Good Morning!!")
	print(f"{" "*(len(user_Name)+8)}My Course is {user_Sub}.My Roll Number is :{user_Roll}")
	print(f"My Address is {user_Address}")

user_Address = input("Enter Your Address:")
user_Roll = int(input("Enter Your Roll Number:"))
Intro("MCA",user_Address,user_Roll,user_Name="Shahnawaz Khan")