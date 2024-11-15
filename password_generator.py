import random
import string
def password_generator():
	pass_len = 8
	Emp= ""
	for i in range(pass_len):
 		Temp=Emp.join(random.choice(string.digits+string.ascii_lowercase+string.ascii_uppercase+string.ascii_letters+string.punctuation))
 		print(Temp) 

password_generator()
