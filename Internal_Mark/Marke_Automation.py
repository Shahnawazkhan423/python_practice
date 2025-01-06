class Inter_Function:
	def create_Deatil(self):
		print("Option 1 Selected")
		stu_Id = int(input("Enter The Student Id Number:"))
		stu_Name = input("Enter The Student Name:")
		stu_Class = input("Enter The Student Class:")
		stu_Contact = int(input("Enter The Student Contact:"))
		stu_Address = input("Enter The Student Address:")
		internal_First = int(input("Enter The First Internal Mark:"))
		internal_Sec = int(input("Enter The Second Internal Mark:"))
		internal_Third = int(input("Enter The Third Internal Mark:"))
		calu_Mark = 0
		grade = ""
		cal_Mark =internal_First + internal_Sec + internal_Third
		if 38<=cal_Mark<=40:
			grade="A+"
		elif 35<=cal_Mark<=37:
			grade="A"
		elif 31<=cal_Mark<=34:
			garde="B+"
		elif 25<=cal_Mark<=30:
			grade="B"
		elif 21<=cal_Mark<=24:
			grade="C+"
		elif 15<=cal_Mark<=20:
			garde="C"
		else:
			grade="Fail"
		entry = "{},{},{},{},{},{},{},{},{},{}\n".format(stu_Id,stu_Name,stu_Class,stu_Contact,stu_Address,internal_First,internal_Sec,internal_Third,cal_Mark,grade)
		file1 = open("Student_Detail.csv","a")
		file1.write(entry)
		print("Contact Added Successfully")
		file1.close()
	def showall_Detail(self):
		print("Option 2 Selected")
		file1 = open("Student_Detail.csv","r")
		Deatil = file1.readlines()
		file1.close()
		for i in Deatil:
			i = i.replace("\n","")
			Deatil_entry = i.split(",")
			print("=================================")
			print("Student ID :",Deatil_entry[0])
			print("Sudent Name :",Deatil_entry[1])
			print("Student Class :",Deatil_entry[2])
			print("Student Contact :",Deatil_entry[3])
			print("Sudent Address :",Deatil_entry[4])
			print("Student First Internal Mark :",Deatil_entry[5])
			print("Student Second Internal Mark :",Deatil_entry[6])
			print("Sudent Third Internal Mark :",Deatil_entry[7])
			print("Student Total Mark :",Deatil_entry[8])
			print("Student Grade :",Deatil_entry[9])
			print("=================================")

	def search_Detail(self):
		print("Option 3 Selected")
		search_choice = input("Enter The Term What You Want to Search in Phone Book:")
		file1 = open("Student_Detail.csv","r")
		contacts = file1.readlines()
		for entry in contacts:
			if search_choice in entry:
				search_choice = search_choice.replace("\n","")
				contact_entry = entry.split(",")
				print("=================================")
				print("Student ID :",Deatil_entry[0])
				print("Sudent Name :",Deatil_entry[1])
				print("Student Class :",Deatil_entry[2])
				print("Student Contact :",Deatil_entry[3])
				print("Sudent Address :",Deatil_entry[4])
				print("Student First Internal Mark :",Deatil_entry[5])
				print("Student Second Internal Mark :",Deatil_entry[6])
				print("Sudent Third Internal Mark :",Deatil_entry[7])
				print("Student Total Mark :",Deatil_entry[8])
				print("Student Grade :",Deatil_entry[9])
				print("=================================")
		file1.close()
	def update_Detail(self):
		print("Option 4 Selected")
		def create(value):
			file1 = open("Student_Detail.csv","r")
			data = file1.readlines()
			file1.close()
			file1=open("Student_Detail.csv","w")
			file1.close()
			file1 = open("Student_Detail.csv","a")
			for line in data:
				if update_chioce not in line:
					file1.write(line)
			file1.close()
		update_chioce = input("Enter The old Value:")
		update_chioce_New = input("Enter The New Value:")
		file1 = open("Student_Detail.csv","r")
		contacts = file1.readlines()
		for entry in contacts:
			if update_chioce in entry:
				update_chioce = update_chioce.replace("\n","")
				contact_entry = entry.split(",")
				print("==============old Record===================")
				print("Student ID :",Deatil_entry[0])
				print("Sudent Name :",Deatil_entry[1])
				print("Student Class :",Deatil_entry[2])
				print("Student Contact :",Deatil_entry[3])
				print("Sudent Address :",Deatil_entry[4])
				print("Student First Internal Mark :",Deatil_entry[5])
				print("Student Second Internal Mark :",Deatil_entry[6])
				print("Sudent Third Internal Mark :",Deatil_entry[7])
				print("Student Total Mark :",Deatil_entry[8])
				print("Student Grade :",Deatil_entry[9])
				print("=================================")
				entry = entry.replace(update_chioce,update_chioce_New)
				update_chioce_New = update_chioce_New.replace("\n","")
				contact_entry = entry.split(",")
				print("==============New Record===================")
				print("Student ID :",Deatil_entry[0])
				print("Sudent Name :",Deatil_entry[1])
				print("Student Class :",Deatil_entry[2])
				print("Student Contact :",Deatil_entry[3])
				print("Sudent Address :",Deatil_entry[4])
				print("Student First Internal Mark :",Deatil_entry[5])
				print("Student Second Internal Mark :",Deatil_entry[6])
				print("Sudent Third Internal Mark :",Deatil_entry[7])
				print("Student Total Mark :",Deatil_entry[8])
				print("Student Grade :",Deatil_entry[9])
				print("=================================")
				print("==============Update Successfully==================")
				file1 = open("Student_Detail.csv","a")
				file1.write(entry)
				file1.close()
				create(update_chioce)
		file1.close()
	def delete_Detail(self):
		print("Option 5 Selected")
		delete_choice = input("Enter The Value:")
		file1 = open("Student_Detail.csv","r")
		data = file1.readlines()
		file1.close()
		file1 = open("Student_Detail.csv","w")
		file1.close()
		file1 = open("Student_Detail.csv","a")
		for line in data:
			if delete_choice not in line:
				file1.write(line)
		print("Delete Successfully")
		file1.close()
		

