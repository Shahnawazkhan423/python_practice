user = int(input("How Many Data Insert:"))#3
dict_Name = {}
dict_Contact = {}
dict_College = {}
dict_Roll_No = {}
index = 0
for i in range(user):
	name = input("Enter The Name:")
	cont = int(input("Enter The Contact Number:"))
	coll = input("Enter The College Name:")
	roll = int(input("Enter The Roll No:"))
	print()
	dict_Name[index]=name
	dict_Contact[index]=cont
	dict_College[index]=coll
	dict_Roll_No[index]=roll
	index+=1
for key in dict_Name:	
	val1 = dict_Name[key]
	val2 = dict_Contact[key]
	val3 = dict_College[key]
	val4 = dict_Roll_No[key]
	print(val1)
	print(val2)
	print(val3)
	print(val4)
	print()
