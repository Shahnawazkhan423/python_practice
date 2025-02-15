import csv
def import_cvs():
	with open("100-contacts.csv",newline="") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			data = (row["first_name"]+","+row["email"]+","+row["phone"]+"\n")
			with open("phone_Book.txt","a") as fileappend:
				fileappend.write(data)
		print("====================Successfully Import==============================")