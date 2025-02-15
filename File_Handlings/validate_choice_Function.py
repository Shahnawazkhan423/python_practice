def mob_num_Valid():
	mob_num = input("Enter The Valid Mobile Number:")
	Numeric = mob_num.isnumeric()
	if len(mob_num)==10 and Numeric is True and :
		return mob_num
	elif Numeric is False:
		print("Invalid Input")
		mob_num_Valid()
	elif len(mob_num)<10 or len(mob_num)>10:
		print("Only 10 Digits Allow")
		mob_num_Valid()
	elif  len(mob_num[0])==0:
		print("Number Not Start 0")
		mob_num_Valid()
	else:
		print("Invalid Syntax")
		mob_num_Valid()

def name_Valid()