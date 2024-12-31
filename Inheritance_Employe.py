class Employee:
	def __init__(self):
		self.emp_Id = input("Enter The Employee Id:")
		self.emp_Name = input("Enter The Employee Name:")
		self.emp_Contact = int(input("Enter The Employee Contact:"))
		self.emp_Email =input("Enter The Employee  Email:") 
		self.emp_Address = input("Enter The Employee Address")
	def show(self):
		print("Employee Data")
		print("Employee Id:",self.emp_Id)
		print("Employee Name:",self.emp_Name)
		print("Employee Contact:",self.emp_Contact)
		print("Employee Email:",self.emp_Email)
		print("Employee Address:",self.emp_Address)
		print("----------------------------------")


class Manager(Employee):
	def __init__(self):
		super().__init__()
		self.department = input("Enter Department : ")
	def show2(self):
		super().show()
		print("Department : ",self.department)

emp = Employee()
emp.show()
emp.show2()

mang = Manager()
mang.show()
mang.show2()