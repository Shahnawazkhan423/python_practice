from validate_choice_Function import*
def create_contact():
	print("Option 1 Selected")
	name = input("Enter Name:")
	email = input("Enter Email:")
	contact = mob_num_Valid()
	entry = "{},{},{}\n".format(name,email,contact)
	file1 = open("phone_Book.txt","a")
	file1.write(entry)
	print("Contact Added Successfully")
	file1.close()
def showall_contact():
	print("Option 2 Selected")
	file1 = open("phone_Book.txt","r")
	contacts = file1.readlines()
	file1.close()
	for i in contacts:
		i = i.replace("\n","")
		contact_entry = i.split(",")
		print("=================================")
		print("Name :",contact_entry[0])
		print("Email :",contact_entry[1])
		print("Contact :",contact_entry[2])
		print("=================================")
def search_contact():
	print("Option 3 Selected")
	search_choice = input("Enter The Term What You Want to Search in Phone Book:")
	file1 = open("phone_Book.txt","r")
	contacts = file1.readlines()
	for entry in contacts:
		if search_choice in entry:
			search_choice = search_choice.replace("\n","")
			contact_entry = entry.split(",")
			print("=================================")
			print("Name :",contact_entry[0])
			print("Email :",contact_entry[1])
			print("Contact :",contact_entry[2])
			print("=================================")
	file1.close()

def update_contact():
	print("Option 4 Selected")
	def create(value):
		file1 = open("phone_Book.txt","r")
		data = file1.readlines()
		file1.close()
		file1=open("phone_Book.txt","w")
		file1.close()
		file1 = open("phone_Book.txt","a")
		for line in data:
			if update_chioce not in line:
				file1.write(line)
		file1.close()
	update_chioce = input("Enter The old Value:")
	update_chioce_New = input("Enter The New Value:")
	file1 = open("phone_Book.txt","r")
	contacts = file1.readlines()
	for entry in contacts:
		if update_chioce in entry:
			update_chioce = update_chioce.replace("\n","")
			contact_entry = entry.split(",")
			print("==============old Record===================")
			print("Name :",contact_entry[0])
			print("Email :",contact_entry[1])
			print("Contact :",contact_entry[2])
			print("=================================")
			entry = entry.replace(update_chioce,update_chioce_New)
			update_chioce_New = update_chioce_New.replace("\n","")
			contact_entry = entry.split(",")
			print("==============New Record===================")
			print("Name :",contact_entry[0])
			print("Email :",contact_entry[1])
			print("Contact :",contact_entry[2])
			print("=================================")
			print("==============Update Successfully==================")
			file1 = open("phone_Book.txt","a")
			file1.write(entry)
			file1.close()
			create(update_chioce)
	file1.close()
def delete_contact():
	print("Option 5 Selected")
	delete_choice = input("Enter The Value:")
	file1 = open("phone_Book.txt","r")
	data = file1.readlines()
	file1.close()
	file1 = open("phone_Book.txt","w")
	file1.close()
	file1 = open("phone_Book.txt","a")
	for line in data:
		if delete_choice not in line:
			file1.write(line)
	print("Delete Successfully")
	file1.close()
	

