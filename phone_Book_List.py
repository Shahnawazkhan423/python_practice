print("Welcome to Phone Book")
print("You Can Any Name and Number Add in Phone Book just Follow Instructuion")
print("Add Name And Number:1\nRemove Any Name And Number:2\nInsert Any Name And Number in position:3\nUpdate Contact Number:4")
chioce = int(input("Enter Value :"))
name = input("Enter The Name: ")	
num = int(input("Enter The Number: "))
phone_list ={}
if chioce==1:
		phone_list[name]=num
		print(phone_list) 

elif chioce==2:
	phone_list.remove(name)
	phone_list.remove(num)
	print(phone_list) 
		
elif chioce==3:	
	name_pos = int(input("Enter The Position:"))
	num_pos = int(input("Enter The Position:"))
	phone_list.insert(name_pos,name)
	phone_list.insert(num_pos,num)
	print(phone_list) 
else:
	print("Invalid Value")



"""
print("Welcome to Phone Book")
print("You Can Any Name and Number Add in Phone Book just Follow Instructuion")
print("Add Name And Number And Update Number:1\nRemove Any Name And Number:2")
chioce = int(input("Enter Value :"))
name_user = input("Enter The Name:")
num_user = int(input("Enter The Number:"))
phone_list ={"Zaid":7067606682,"Khan":9981883263}
if chioce==1:
    phone_list[name_user]=num_user
    print(phone_list)
elif chioce==2:
    phone_list.pop(name_user)
    print(phone_list)
else:
    print("Invalid Synatx")
"""