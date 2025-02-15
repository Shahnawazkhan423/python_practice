import csv
def export():
	with open("phone_Book.txt",newline="") as data:
		reader = csv.DictReader(data)
		with open("contacts.csv","w") as csvfile:
			write = csv.writer(csvfile)
			for row in data:
				row = row.replace("\n","")
				data =row.split(",")
				write.writerow(data)
			print("====================Successfully Export==============================")